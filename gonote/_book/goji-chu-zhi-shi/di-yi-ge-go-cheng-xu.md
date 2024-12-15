# Go 语言教程

```
Go 是一个开源的编程语言，它能让构造简单、可靠且高效的软件变得容易。

Go是从2007年末由Robert Griesemer, Rob Pike, Ken Thompson主持开发，后来还加入了Ian Lance Taylor, Russ Cox等人，并最终于2009年11月开源，在2012年早些时候发布了Go 1稳定版本。现在Go的开发已经是完全开放的，并且拥有一个活跃的社区。
```

## Go 语言特色

- 简洁、快速、安全
- 并行、有趣、开源
- 内存管理、数组安全、编译迅速

## Go 语言用途

```
Go 语言被设计成一门应用于搭载 Web 服务器，存储集群或类似用途的巨型中央服务器的系统编程语言。

对于高性能分布式系统领域而言，Go 语言无疑比大多数其它语言有着更高的开发效率。它提供了海量并行的支持，这对于游戏服务端的开发而言是再好不过了。
```

## 第一个 Go 程序

接下来我们来编写第一个 Go 程序 hello.go（Go 语言源文件的扩展是 .go），代码如下：

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```



运行

```go
$ go run hello.go 
Hello, World!
```



##### 此外我们还可以使用 **go build** 命令来生成二进制文件：

```go
$ go build hello.go 
$ ls
hello    hello.go
$ ./hello 
Hello, World!
```

执行命令

```yacas
E:\go\代码\Project\基础\hello_word\main>go run hello_word.go
Hello WordHello Word
Hello Word

E:\go\代码\Project\基础\hello_word\main>go build

E:\go\代码\Project\基础\hello_word\main>dir
驱动器 E 中的卷是 study
卷的序列号是 DCA4-4E82

E:\go\代码\Project\基础\hello_word\main 的目录

2021/05/31  23:10    <DIR>          .
2021/05/31  23:10    <DIR>          ..
2021/05/31  23:09               480 hello_word.go
2021/05/31  23:10         2,144,256 main.exe
2 个文件      2,144,736 字节
2 个目录 108,196,679,680 可用字节

E:\go\代码\Project\基础\hello_word\main>go build hello_word.go

E:\go\代码\Project\基础\hello_word\main>dir
驱动器 E 中的卷是 study
卷的序列号是 DCA4-4E82

E:\go\代码\Project\基础\hello_word\main 的目录

2021/05/31  23:10    <DIR>          .
2021/05/31  23:10    <DIR>          ..
2021/05/31  23:10         2,144,256 hello_word.exe
2021/05/31  23:09               480 hello_word.go
2021/05/31  23:10         2,144,256 main.exe
3 个文件      4,288,992 字节
2 个目录 108,194,533,376 可用字节

E:\go\代码\Project\基础\hello_word\main>go build -o hello hello_word.go

E:\go\代码\Project\基础\hello_word\main>dir
驱动器 E 中的卷是 study
卷的序列号是 DCA4-4E82

E:\go\代码\Project\基础\hello_word\main 的目录

2021/05/31  23:11    <DIR>          .
2021/05/31  23:11    <DIR>          ..
2021/05/31  23:11         2,144,256 hello
2021/05/31  23:10         2,144,256 hello_word.exe
2021/05/31  23:09               480 hello_word.go
2021/05/31  23:10         2,144,256 main.exe
4 个文件      6,433,248 字节
2 个目录 108,192,387,072 可用字节
```

转义符 \

```
\t 相当于一个table 
\n 换行
\t 
\\ 
```

