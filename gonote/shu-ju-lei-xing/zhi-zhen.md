## 关于指针 {#_01-关于指针}

要搞明白**Go**语言中的指针需要先知道**3**个概念：`指针地址、指针类型、指针取值`

* `指针地址（&a）`

* `指针取值（*&a）`

* `指针类型（&a）`—&gt;`*int`改变数据传指针

* 变量的本质是给存储数据的内存地址起了一个好记的别名。

* 比如我们定义了一个变量 a := 10 ,这个时候可以直接通过 a 这个变量来读取内存中保存的 10 这个值。

* 在计算机底层 a 这个变量其实对应了一个内存地址。

* 指针也是一个变量，但它是一种特殊的变量，它存储的数据不是一个普通的值，而是另一个变量的内存地址。

* **Go**语言中的指针操作非常简单，我们只需要记住两个符号：&（取地址）和 \*（根据地址取值）

```go
package main

import "fmt"

func pointer() {
    a := 10
    // 值
    fmt.Printf("%d \n", a)
    // 指针地址
    fmt.Printf("%d \n", &a)
    // 去内存地址取值
    fmt.Printf("%d \n", *&a)
    // 指针类型
    fmt.Printf("%T \n", &a)
}

func main() {
    pointer()
}
```

![](/assets/import100.png)

![](http://v5blog.cn/assets/img/image-20210519103732255.5c4eeb04.png)

## `&取变量地址` {#_02-取变量地址}

### &符号取地址操作 {#_2-1-符号取地址操作}

* 每个变量在运行时都拥有一个地址，这个地址代表变量在内存中的位置。

* Go 语言中使用&字符放在变量前面对变量进行取地址操作。

* Go 语言中的值类型（int、float、bool、string、array、struct）都有对应的指针类型

* 取变量指针的语法如下：

```go
ptr := &v      // 比如 v 的类型为 T
```

* **v**: 代表被取地址的变量，类型为 T

* **ptr**: 用于接收地址的变量，**ptr**的类型就为\*T，称做 T 的指针类型。\*代表指针。

```go
package main

import "fmt"

func pointer2() {
    a := 10
    b := &a
    fmt.Printf("%d prt: %p \n", a, &a)
    fmt.Printf("%v type: %T \n", b, b)
    fmt.Printf("取b的地址 %d", &b)
}

func main() {
    pointer2()
}
```

![](/assets/import101.png)

### b := &a 的图示 {#_2-2-b-a-的图示}

![](http://v5blog.cn/assets/img/image-20210519104530628.569190a8.png)

## 指针修改数据 {#_03-指针修改数据}

### `*指针取值` {#_3-1-指针取值}

* 在对普通变量使用
  &
  操作符取地址后会获得这个变量的指针，然后可以对指针使用操作，也就是指针取值

```go
package main

import "fmt"

func pointer3() {
    a := 10
    b := &a
    fmt.Printf("type: %T \n", b)
    c := *b
    fmt.Printf("value: %d type: %[1]T \n", c)
}

func main() {
    pointer3()
}
```

![](/assets/import102.png)

* 变量、指针地址、指针变量、取地址、取值的相互关系和特性如下：

  * 对变量进行取地址（&）操作，可以获得这个变量的指针变量。

  * 指针变量的值是指针地址。

  * 对指针变量进行取值（\*）操作，可以获得指针变量指向的原变量的值。

### 指针传值示例 {#_3-2-指针传值示例}

```go
package main

import "fmt"

func pointer5(x *int) {
    *x = 9
    fmt.Printf("value: %d type: %[1]T \n", x)
    fmt.Printf("value: %d type: %[1]T \n", *x)
}

func main() {
    var a = 10
    pointer4(a)
    fmt.Println(a)
    pointer5(&a)
    fmt.Println(a)
}
```

![](/assets/import104.png)

## new 和 make {#_04-new-和-make}

### 执行报错 {#_4-0-执行报错}

* 执行下面的代码会引发 panic，为什么呢？
* 在 Go 语言中对于引用类型的变量，我们在使用的时候不仅要声明它，还要为它分配内存空间，否则我们的值就没办法存储。
* 而对于值类型的声明不需要分配内存空间，是因为它们在声明的时候已经默认分配好了内存空间。
* 要分配内存，就引出来今天的 new 和 make。
* Go 语言中 new 和 make 是内建的两个函数，主要用来分配内存。

```go
package main

import "fmt"

func main() {
    var a map[string]string
    a["name"] = "张三"
    fmt.Println(a)
}
```

![](/assets/import105.png)

### make和new比较 {#_4-1-make和new比较}

* new 和 make 是两个内置函数，主要用来创建并分配类型的内存。

* make和new区别

  * `make`
    关键字的作用是创建于 slice、map 和 channel 等内置的数据结构
  * `new`
    的作用是为类型申请一片内存空间，并返回指向这片内存的指针

```go
package main

import "fmt"

func createMake() {
    a := make(map[string]string)
    a["name"] = "张三"
    fmt.Println(a)

    b := make([]int, 2, 5)
    b = append(b, 5)
    fmt.Println(b)

    b1 := new([]int)
    *b1 = append(*b1, 3)
    fmt.Println(b1)

}

func main() {
    createMake()
}
```

![](/assets/import106.png)

### new函数 {#_4-2-new函数}

* `一：系统默认的数据类型，分配空间`

```go
package main

import "fmt"

func createNew() {
    // 实例化int
    a := new(int)
    *a = 10
    fmt.Printf("value %d, type %[1]T \n", *a)
    // 实例化slice
    b := new([]int)
    *b = append(*b, 3)
    fmt.Printf("value %d, type %[1]T \n", *b)
    // 实例化map
    c := new(map[string]string)
    *c = map[string]string{}
    (*c)["name"] = "张三"
    fmt.Printf("value %v, type %[1]T \n", *c)
}

func main() {
    createNew()
}
```

![](/assets/import107.png)

* `二：自定义类型使用 new 函数来分配空间`

```go
package main

import "fmt"

type people struct {
    name string
    age  int
}

func main() {
    var a *people
    // 分配空间
    a = new(people)
    a.name = "张三"
    fmt.Printf("value %v, type %[1]T \n", a)
}
```

### ![](/assets/import108.png) {#_4-3-make函数}

### make函数 {#_4-3-make函数}

* make 也是用于内存分配的，但是和 new 不同，它只用于 chan、map 以及 slice 的内存创建
* 而且它返回的类型就是这三个类型本身，而不是他们的指针类型
* 因为这三种类型就是引用类型，所以就没有必要返回他们的指针了

```go
package main

import "fmt"

func main() {
    a := make([]int, 2, 4)
    b := make(map[string]int)
    var c = make(chan int, 1)
    fmt.Printf("value %v, type %[1]T \n", a)
    fmt.Printf("value %v, type %[1]T \n", b)
    fmt.Printf("value %v, type %[1]T \n", c)
}
```

![](/assets/import109.png)

* 当我们为slice分配内存的时候，应当尽量预估到slice可能的最大长度
* 通过给make传第三个参数的方式来给slice预留好内存空间
* 这样可以避免二次分配内存带来的开销，大大提高程序的性能。 



