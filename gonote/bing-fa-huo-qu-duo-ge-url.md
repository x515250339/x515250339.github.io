go语言圣经-并发获取多个URL

1.GO最新奇的特性就是对并发编程的支持,goroutine和channel

2.goroutine是一种函数的并发执行方式，而channel是用来在goroutine之间进行参数传递

  go function则表示创建一个新的goroutine，并在这个新的goroutine中执行这个函数。

3.make函数创建了一个传递string类型参数的channel

4.io.Copy把响应的Body内容拷贝到ioutil.Discard输出流中,扔到一个垃圾桶

5.goroutine尝试在一个channel上做send或者receive操作时，这个goroutine会阻塞在调用处,直到另一个goroutine往这个channel里写入、或者接收值

6.用main函数来接收所有fetch函数传回的字符串，可以避免在goroutine异步执行还没有完成时main函数提前退出。





练习 1.10： 找一个数据量比较大的网站，用本小节中的程序调研网站的缓存策略，对每个URL执行两遍请求，查看两次时间是否有较大的差别，并且每次获取到的响应内容是否一致，修改本节中的程序，将响应结果输出，以便于进行对比。

练习 1.11： 在fetchall中尝试使用长一些的参数列表，比如使用在alexa.com的上百万网站里排名靠前的。如果一个网站没有回应，程序将采取怎样的行为？

（Section8.9 描述了在这种情况下的应对机制）。

```go
package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	"time"
)

func main() {
	// 获取当前时间
	start := time.Now()
	// make函数创建了一个传递string类型参数的channel
	ch := make(chan string)
	// for循环命令行参数
	for _, url := range os.Args[1:] {
		// 开启一个goroutine
		go fetch(url, ch)
	}
	for range os.Args[1:] {
		// 接收并打印channel,for循环不需要key value
		fmt.Println(<-ch)
	}
	// main函数的执行时间
	fmt.Printf("%.2fs elapsed\n", time.Since(start).Seconds())
}

// 参数类型:string , chan<- string
func fetch(url string, ch chan<- string) {
	start := time.Now()
	resp, err := http.Get(url)
	if err != nil {
		ch <- fmt.Sprint(err)
		return
	}
	// 把内容扔掉,只获取字节数
	nbytes, err := io.Copy(ioutil.Discard, resp.Body)
	resp.Body.Close()

	if err != nil {
		ch <- fmt.Sprintf("while reading %s: %v", url, err)
		return
	}
	// 记录执行的秒数
	secs := time.Since(start).Seconds()
	// 发送给channel
	ch <- fmt.Sprintf("%.2fs %7d %s", secs, nbytes, url)

}

```

![](/assets/import9.png)

