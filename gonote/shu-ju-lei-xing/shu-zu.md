# 数组介绍

### Array介绍 {#_1-1-array介绍}

* 数组是指一系列
  `同一类型数据的集合`。
* 数组中包含的每个数据被称为数组元素\(element\)，这种类型可以是任意的原始类型，比如 int、string 等
* 一个数组包含的元素个数被称为数组的长度。
* 在 Golang 中数组是一个长度固定的数据类型，数组的长度是类型的一部分，也就是说
  `[5]int 和 [10]int 是两个不同的类型`。
* Golang中数组的另一个特点是占用内存的连续性，也就是说数组中的元素是被分配到连续的内存地址中的，因而索引数组元素的速度非常快。
* 和数组对应的类型是 Slice（切片），Slice 是可以增长和收缩的动态序列，功能也更灵活
* 但是想要理解 slice 工作原理的话需要先理解数组，所以本节主要为大家讲解数组的使用。

![](http://v5blog.cn/assets/img/image-20210518110223971.b3f1bc7a.png)

### 数组定义 {#_1-2-数组定义}

```go
var 数组变量名 [元素数量]T
```

* 比如：var a \[5\]int， 数组的长度必须是常量，并且长度是数组类型的一部分
* 一旦定义，长度不能变。 \[5\]int 和\[4\]int 是不同的类型。

```go
package main

import "fmt"

// 创建数组并赋值
func createArr() {
    // 创建数组 5 个元素 int 类型
    var a [5]int
    // 创建数组 3 个元素 int 类型
    var b [3]int
    fmt.Printf("类型：%T value：%[1]v \n", a)
    fmt.Printf("类型：%T value：%[1]v \n", b)
    // 进行下标取值并赋值 0 开始
    a[0] = 11
    a[3] = 33
    b[0] = 22
    b[2] = 99
    fmt.Printf("类型：%T value：%[1]v \n", a)
    fmt.Printf("类型：%T value：%[1]v \n", b)
}

func main() {
    createArr()
}
```

![](/assets/import52.png) {\#\_1-3-数组是值类型}

### 数组是值类型 {#_1-3-数组是值类型}

* 数组是值类型，赋值和传参会复制整个数组。

* 因此改变副本的值，不会改变本身的值。

* 注意：

  * 数组支持 “==“、”!=” 操作符，因为内存总是被初始化过的。
  * `[n]*T`
    表示指针数组，
    `*[n]T`
    表示数组指针

```go
package main

import "fmt"

// 数组是值类型
func updateArr(x [3]int) {
    x[2] = 100
    fmt.Println("【updateArr】-- 修改值为副本不影响本身的值", x)
}

// 数组是值类型
func updateArr2(x *[3]int) {
    x[2] = 100
    fmt.Println("【updateArr】-- 修改值为本身", *x)
}

func main() {
    // 数组是值类型
    var a [3]int
    updateArr(a)
    fmt.Println(a)
    fmt.Println()
    // 修改本身需要传递内存地址
    var b [3]int
    updateArr2(&b)
    fmt.Println(b)
}
```

![](/assets/import53.png)

## 创建数组 {#_02-创建数组}

### 自定义数组长度 {#_2-1-自定义数组长度}

```go
package main

import "fmt"

func createCustomArr() {
    var a [3]int
    fmt.Println(a)

    var b = [3]int{1, 2}
    fmt.Println(b)
}

func main() {
    createCustomArr()
}
```

![](/assets/import54.png)

### 让编译器识别 {#_2-2-让编译器识别}

* 按照上面的方法每次都要确保提供的初始值和数组长度一致
* 一般情况下我们可以让编译器根据初始值的个数自行推断数组的长度

```go
package main

import "fmt"

func createCustomArr2() {
    // 不定长Arr
    var c = []string{"张三", "李四"}
    fmt.Printf("类型：%T  value：%[1]v \n", c)
    // 不定长Arr 两个参数长度就为2
    var d = [...]string{"张三", "dd"}
    fmt.Printf("类型：%T  value：%[1]v \n", d)
    // 不定长Arr 长度默认下标加1 4+1=5
    var e = [...]int{0: 3, 1: 5, 4: 6}
    fmt.Printf("类型：%T  value：%[1]v \n", e)

}

func main() {
    createCustomArr2()
}
```

![](/assets/import55.png)

### 指定索引值 {#_2-3-指定索引值}

* 我们还可以使用指定索引值的方式来初始化数组

```go
package main

import "fmt"

func createCustomArr3() {
    // 指定索引赋值 长度默认下标加1 4+1=5
    var e = [...]int{0: 3, 1: 5, 4: 6}
    fmt.Printf("类型：%T  value：%[1]v \n", e)
}


func main() {
    createCustomArr3()
}
```

![](/assets/import56.png)

## 数组的遍历 {#_03-数组的遍历}

### 普通遍历数组 {#_3-1-普通遍历数组}

```go
package main

import (
    "fmt"
)

func main() {
    // 普通遍历
    var a = [...]int{998, 2, 3}
    for x := 0; x < len(a); x++ {
        fmt.Println(a[x])
    }
}
```

![](/assets/import57.png)

### k,v遍历数组 {#_3-2-k-v遍历数组}

```go
package main

import (
    "fmt"
)

func main() {
    var a = [...]int{998, 2, 3}
    // k,v遍历
    for k, v := range a {
        fmt.Println(k, v)
    }
}
```

![](/assets/import58.png)

##  {#_04-多维数组}

## 多维数组 {#_04-多维数组}

### 定义多维数组 {#_4-1-定义多维数组}

```go
package main

import "fmt"

func manyArr() {
    var a = [3][2]string{
        {"张三", "男"},
        {"里斯", "女"},
        {"老六", "中"},
    }
    fmt.Println(a)
    fmt.Println(a[1][0])

}

func main() {
    manyArr()
}
```

![](/assets/import59.png)

### 遍历多维数组 {#_4-2-遍历多维数组}

```go
package main

import "fmt"

func manyArr() [3][2]string {
    var a = [3][2]string{
        {"张三", "男"},
        {"里斯", "女"},
        {"老六", "中"},
    }
    //fmt.Println(a)
    //fmt.Println(a[1][0])
    return a
}

func main() {
    a := manyArr()
    for _, i := range a {
        var name string
        var sex string
        for k, v := range i {
            if k == 0 {
                name = v
                continue
            } else if k == 1 {
                sex = v
            }
            fmt.Println("name:", name, "sex:", sex)

        }
    }
}
```

![](/assets/import66.png)

## 数组练习 {#_05-数组练习}

### 数组求和 {#_5-1-数组求和}

```go
package main

import "fmt"

func sumArr(a [3]int) {
    sum := 0
    for _, i := range a {
        sum += i
    }
    fmt.Printf("sum: %v, mean: %v", sum, float64(sum)/float64(len(a)))
}

func main() {
    var a = [...]int{998, 2, 3}
    sumArr(a)
}
```

![](/assets/import64.png)

### 数组最大值 {#_5-2-数组最大值}

* 1、声明一个数组 var intArr\[5\] = \[...\]int {1, -1, 12, 65, 11}

* 2、假定第一个元素就是最大值，下标就 0

* 3、然后从第二个元素开始循环比较，如果发现有更大，则交换

```go
package main

import "fmt"

func maxArr() {
    a := [4]int{1, 2, 4, 3}
    var max int = a[0]
    for _, i := range a {
        if i > max {
            max = i
        }
    }
    fmt.Println(max)
}

func main() {
    maxArr()
}
```

![](/assets/import68.png)

