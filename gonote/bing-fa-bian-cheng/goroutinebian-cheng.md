# goroutine编程

## goroutine池

- 本质上是生产者消费者模型
- 在工作中我们通常会使用可以指定启动的goroutine数量–`worker pool`模式，控制`goroutine`的数量，防止`goroutine`泄漏和暴涨。
- 一个简易的`work pool`示例代码如下：

```go
package main

import (
	"fmt"
	"time"
)

func worker(id int, jobs <-chan int, results chan<- int) {
	// 消费者消费任务
	for j := range jobs {
		fmt.Printf("worker:%d start job:%d\n", id, j)
		time.Sleep(time.Second)
		fmt.Printf("worker:%d end job:%d\n", id, j)
		results <- j * 2
	}
}

func main() {
	jobs := make(chan int, 100)
	results := make(chan int, 100)
	// 1）开启3个goroutine,作为消费者消费 jobs中任务
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}
	// 2）5个任务（生产者生产任务）
	for j := 1; j <= 5; j++ {
		jobs <- j
	}
	close(jobs)
	// 3）输出结果
	for a := 1; a <= 5; a++ {
		v := <-results
		fmt.Println(v)
	}
}
```

## 打印奇数偶数

### 一个无缓冲管道实现

- 首先我们这里通过make(chan int)，开辟的通道是一种无缓冲通道
- 所以当对这个缓冲通道写的时候，`会一直阻塞等到某个协程对这个缓冲通道读`
- 而这里我讲 `ch <- true 理解为生产`，他却是`需要等到某个协程读了再能继续运行`

```go
package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func printJS(ch chan bool) {
	defer wg.Done()
	for i := 1; i <= 9; i += 2 {
		fmt.Println("js", i)   // 奇数先打印
        ch <- true         // 给偶数打印函数一个信号(需要等到某个协程读了再能继续运行)
		<-ch
	}
}

func printOS(ch chan bool) {
	defer wg.Done()
	for i := 2; i <= 10; i += 2 {
		<-ch  // 偶数等待奇数函数 向chan发送信号
		fmt.Println("os", i)
		ch <- false         // 给奇数打印函数一个信号(需要等到某个协程读了再能继续运行)
	}
}

func main() {
	// 新建一个无缓冲管道（无缓冲管道只能一个协程写入，然后另外一个协程来读取）
	ch := make(chan bool)
	wg.Add(2)
	go printJS(ch)
	go printOS(ch)
	wg.Wait()
}
```

### 两个无缓冲管道实现

```go
package main

import (
	"fmt"
	"sync"
)

var ch1 = make(chan bool)
var ch2 = make(chan bool)
var wg sync.WaitGroup

func go1JS() {
	defer wg.Done()
	for i := 1; i <= 10; i += 2 {
		<-ch1 // ch1获取数据成功就不阻塞，进行下一步
		fmt.Println(i)
		ch2 <- true // 向ch2发送信号，打印奇数
	}
	<-ch1  // 因为main函数最初向ch1放入了一个数据，所以最后打印结束后取出，否则死锁
}
func go2OS() {
	defer wg.Done()
	for i := 2; i <= 10; i += 2 {
		<-ch2
		fmt.Println(i)
		ch1 <- true
	}
}
func main() {
	wg.Add(2)
	go go1JS()  // 打印奇数
	go go2OS()  // 打印偶数
	ch1 <- true // 先让奇数的协程执行
	wg.Wait()
}
```

## 超时控制

### 基础版

```go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

// 在 main 函数里调用给定的 rpc 方法，并设置超时时间为 10 秒
// 在等待过程中如果超时则取消等待并打印 "timeout" ，如果没有超时则打印出 rpc 的返回结果。
// rpc 方法不可以修改
func main() {
	ch := make(chan bool)
	var ret int
	go func() {
		ret = rpc()
		<-ch
	}()

	count := 0
	for count < 10 {
		if ret != 0 {
			fmt.Println(ret)
			break
		}
		time.Sleep(time.Second)
		count += 1
	}
	if count >= 10 {
		ch <- false
		fmt.Println("timeout")
	}
}

// 这是你要调用的方法，可以看作一个黑盒
// 它的耗时是 1~15 秒内的随机数
// 最终返回一个随机的 int 类型
func rpc() int {
	cost := rand.Intn(15) + 1
	fmt.Printf("rpc will cost %d seconds\n", cost)
	time.Sleep(time.Duration(cost) * time.Second)
	return cost
}

func init() {
	rand.Seed(time.Now().UnixNano())
}
```

### time.After控制超时

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	workDoneCh := make(chan bool, 1)
	go func() {
		LongTimeWork()     //这是我们要控制超时的函数
		workDoneCh <- true // 函数正常执行结束给 chan信号正常退出
	}()
	select {
	case <-workDoneCh: // 当协程执行完成后会向这个 channel 发送一个数据，收到即可结束
		fmt.Println("Success!")
	case <-time.After(3 * time.Second): //timeout到来
		fmt.Println("timeout") // 3s无返回超时退出
	}
}

func LongTimeWork() {
	time.Sleep(time.Second * 2)
}
```

