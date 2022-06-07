## select 多路复用

### select说明

- 传统的方法在遍历管道时，如果不关闭会阻塞而导致 deadlock，在实际开发中，可能我们不好确定什么关闭该管道。
- 这种方式虽然可以实现从多个管道接收值的需求，但是运行性能会差很多。
- 为了应对这种场景，Go 内置了 select 关键字，可以同时响应多个管道的操作。
- select 的使用类似于 switch 语句，它有一系列 case 分支和一个默认的分支。
- 每个 case 会对应一个管道的通信（接收或发送）过程。
- select 会一直等待，直到某个 case 的通信操作完成时，就会执行 case 分支对应的语句。
- 具体格式如下：

```go
    select {
    case <-chan1:
       // 如果chan1成功读到数据，则进行该case处理语句
    case chan2 <- 1:
       // 如果成功向chan2写入数据，则进行该case处理语句
    default:
       // 如果上面都没有成功，则进入default处理流程
    }
```

### select 的使用

- 使用 select 语句能提高代码的可读性。
- 可处理一个或多个 channel 的发送/接收操作。
- 如果多个 case 同时满足，select 会随机选择一个。
- 对于没有 case 的 select{}会一直等待，可用于阻塞 main 函数。

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	// 在某些场景下我们需要同时从多个通道接收数据,这个时候就可以用到golang中给我们提供的select多路复用

	//1.定义一个管道 10个数据int
	intChan := make(chan int, 10)
	for i := 0; i < 10; i++ {
		intChan <- i
	}

	//2.定义一个管道 5个数据string
	stringChan := make(chan string, 5)
	for i := 0; i < 5; i++ {
		stringChan <- "hello" + fmt.Sprintf("%d", i)
	}

	//使用select来获取channel里面的数据的时候不需要关闭channel
	for {
		select {
		case v := <-intChan:
			fmt.Printf("从 intChan 读取的数据%d \n", v)
			time.Sleep(time.Millisecond * 50)
		case v := <-stringChan:
			fmt.Printf("从 stringChan 读取的数据%s \n", v)
			time.Sleep(time.Millisecond * 50)
		default:
			fmt.Println("数据获取完毕")
			return // 注意推出
		}
	}
}

```

![20220426_184819 00_00_00-00_00_30](../images/select.assets/20220426_184819%2000_00_00-00_00_30.gif)