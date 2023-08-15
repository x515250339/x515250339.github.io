## 切片基础 {#_01-切片基础}

### 切片的定义 {#_1-1-切片的定义}

* 切片（Slice）是一个拥有相同类型元素的可变长度的序列。

* 它是基于数组类型做的一层封装。

* 它非常灵活，支持自动扩容。

* 切片是一个引用类型，它的内部结构包含地址、长度和容量。

* 声明切片类型的基本语法如下：

```go
// var name []T
// 1、name:表示变量名
// 2、T:表示切片中的元素类型
```

```go
package main

import "fmt"

func createSlice() {
    // 切片是引用类型，不支持直接比较，只能和 nil 比较

    //声明一个字符串切片
    var a []string
    fmt.Println(a)
    fmt.Println(a == nil)

    //声明一个字符串切片并初始化
    var b = []string{}
    fmt.Println(b)
    fmt.Println(b == nil)

    //声明一个布尔切片并初始化赋值
    var c = []bool{false}
    fmt.Println(c)
    fmt.Println(c == nil)
}

func main() {
    createSlice()
}
```

![](/assets/import71.png)

切片之间是不能比较的，我们不能使用==操作符来判断两个切片是否含有全部相等元素。

* 切片唯一合法的比较操作是和 nil 比较。 一个 nil 值的切片并没有底层数组，一个 nil 值的切片的长度和容量都是 0。
* 但是我们不能说一个长度和容量都是 0 的切片一定是 nil
* 例如下面的

### 关于 nil 的认识 {#_1-2-关于-nil-的认识}

* 当你声明了一个变量 , 但却还并没有赋值时 , golang 中会自动给你的变量赋值一个默认零值。

* 这是每种类型对应的零值

```go
bool -> false
numbers -> 0
string-> ""
pointers -> nil
slices -> nil
maps -> nil
channels -> nil
functions -> nil
interfaces -> nil
```

### 切片的本质 {#_1-3-切片的本质}

* 切片的本质就是对底层数组的封装，它包含了三个信息：底层数组的指针、切片的长度（len）和切片的容量（cap）。

* 举个例子，现在有一个数组 a := \[8\]int{0, 1, 2, 3, 4, 5, 6, 7}，切片 s1 := a\[:5\]，相应示意图如下。

![](/assets/import69.png)

* 切片 s2 := a\[3:6\]，相应示意图如下![](/assets/import70.png)

### 切片的扩容策略 {#_1-4-切片的扩容策略}

* 1、首先判断，如果新申请容量（cap）大于 2 倍的旧容量（old.cap），最终容量（newcap）就是新申请的容量（cap）。
* 2、否则判断，如果旧切片的长度小于 1024，则最终容量\(newcap\)就是旧容量\(old.cap\)的两倍，即（newcap=doublecap）
* 3、否则判断，如果旧切片长度大于等于 1024，则最终容量（newcap）从旧容量（old.cap）开始循环增加原来的 1/4，即（newcap=old.cap,for{newcap+= newcap/4}）直到最终容量newcap）大于等于新申请的容量\(cap\)，即（newcap 
  &gt;
  = cap）
* 4、如果最终容量（cap）计算值溢出，则最终容量（cap）就是新申请容量（cap）。

### 切片的长度和容量 {#_1-5-切片的长度和容量}

* 切片拥有自己的长度和容量，我们可以通过使用内置的 \*\*len\(\)\*\*函数求长度，使用内置的 \*\*cap\(\)\*\*函数求切片的容量。

* 切片的长度就是它所包含的元素个数。

* 切片的容量是从它的第一个元素开始数，到其底层数组元素末尾的个数。

* 切片 s 的长度和容量可通过表达式 len\(s\) 和 cap\(s\) 来获取。

```go
package main

import "fmt"

// 切片的长度和容量
func showCap() {
    //声明一个字符串切片
    var a = []int{2, 3, 4, 5}
    fmt.Printf("长度%v 容量%v 值%v \n", len(a), cap(a), a)

    b := a[:2]
    fmt.Printf("长度%v 容量%v 值%v \n", len(b), cap(b), b)

    b = a[1:4]
    fmt.Printf("长度%v 容量%v 值%v \n", len(b), cap(b), b)
}

func main() {
    showCap()
}
```

![](/assets/import72.png)

## 切片循环 {#_02-切片循环}

* 切片的循环遍历和数组的循环遍历是一样的

### 基本遍历 {#_2-1-基本遍历}

```go
package main

import "fmt"

func forSlice(a *[]string) {
    // *a[i] 语法错误 可以理解为 *(a[i]) 应当 (*a)[i]
    for i := 0; i < len(*a); i++ {
        fmt.Println((*a)[i])
    }
}

func main() {
    var a = []string{"test1", "test2", "test3"}
    forSlice(&a)
}
```

![](/assets/import73.png)

### k，v遍历 {#_2-2-k，v遍历}

```go
package main

import "fmt"

func kv_forSlice(a *[]string) {
    for k, v := range *a {
        fmt.Println(k, v)
    }
}

func main() {
    var a = []string{"test1", "test2", "test3"}
    kv_forSlice(&a)
}
```

![](/assets/import74.png)

## 定义切片 {#_03-定义切片}

### 数组定义切片 {#_3-1-数组定义切片}

* 由于切片的底层就是一个数组，所以我们可以基于数组定义切片。

```go
package main

import "fmt"

func createArraySlice() {
    var a = [5]int{1, 2, 3, 4, 5}
    b := a[1:3]
    fmt.Printf("类型%T value%[1]v \n", a)
    fmt.Printf("类型%T value%[1]v \n", b)
    c := b[:1]
    fmt.Printf("类型%T value%[1]v \n", c)
}

func main() {
    createArraySlice()
}
```

![](/assets/import75.png)

### make\(\)构造切片 {#_3-2-make-构造切片}

* 我们上面都是基于数组来创建的切片，如果需要动态的创建一个切片，我们就需要使用内置的 make\(\)函数

* 格式如下：`make([]T, size, cap)`

  * T:切片的元素类型

  * size:切片中元素的数量

  * cap:切片的容量

```
package main

import "fmt"

func makeCreateSlice() {
    // Type, size cap
    a := make([]int ,2 ,10)
    fmt.Printf("长度%v 容量%v 值%v \n", len(a), cap(a), a)
}

func main() {
    makeCreateSlice()
}
```

* 上面代码中 a 的内部存储空间已经分配了 10 个，但实际上只用了 2 个。
* 容量并不会影响当前元素的个数，所以 len\(a\)返回 2，cap\(a\)则返回该切片的容量。

![](/assets/import80.png)

## append\(\) {#_04-append}

* Go 语言的内建函数 append\(\)可以为切片动态添加元素，每个切片会指向一个底层数组
* 这个数组的容量够用就添加新增元素。
* 当底层数组不能容纳新增的元素时，切片就会自动按照一定的策略进行“扩容”，此时该切片指向的底层数组就会更换。
* “扩容”操作往往发生在append\(\)函数调用时，所以我们通常都需要用原变量接收 append 函数的返回值。

### append添加 {#_4-1-append添加}

```go
package main

import "fmt"

func appendMethod() {
    a := make([]int, 2, 3)
    a = append(a, 10)
    fmt.Printf("长度%v 容量%v 值%v \n", len(a), cap(a), a)
    a = append(a, 100)
    // 容量不够则 double
    fmt.Printf("长度%v 容量%v 值%v \n", len(a), cap(a), a)
}

func main() {
    appendMethod()
}
```

![](/assets/import81.png)

### append追加多个 {#_4-2-append追加多个}

```go
package main

import "fmt"

func appendMethod() {
    a := make([]int, 2, 3)
    a = append(a, 10)
    fmt.Printf("长度%v 容量%v 值%v \n", len(a), cap(a), a)
    a = append(a, 100)
    fmt.Printf("长度%v 容量%v 值%v \n", len(a), cap(a), a)
}

func main() {
    appendManyMethod()
}
```

![](/assets/import83.png)

### 切片中删除元素 {#_4-3-切片中删除元素}

* Go 语言中并没有删除切片元素的专用方法，我们可以使用切片本身的特性来删除元素

```go
package main

import "fmt"

func delMethod() {
    a := []int{1, 2, 3, 4, 5, 6, 7}
    fmt.Printf("长度%v 容量%v 值%v \n", len(a), cap(a), a)
    a = append(a[:2], a[3:]...)
    fmt.Printf("长度%v 容量%v 值%v \n", len(a), cap(a), a)
}

func main() {
    delMethod()
}
```

![](/assets/import84.png)

### 切片合并 {#_4-4-切片合并}

```go
package main

import "fmt"

func mergeSlice() {
    a := []int{1, 2, 3}
    b := []int{4, 5, 6, 7}
    c := append(a, b...)
    fmt.Printf("长度%v 容量%v 值%v \n", len(c), cap(c), c)
}

func main() {
    mergeSlice()
}
```

![](/assets/import85.png)

## copy\(\) {#_05-copy}

### 引用问题 {#_5-1-引用问题}

* 直接引用为浅拷贝

```go
package main

import "fmt"

func copySlice() {
    a := []int{1, 2, 3, 4}
    fmt.Printf("长度%v 容量%v 值%v \n", len(a), cap(a), a)
    b := a
    fmt.Printf("长度%v 容量%v 值%v \n", len(b), cap(b), b)
    b[0] = 998
    fmt.Printf("a 长度%v 容量%v 值%v \n", len(a), cap(a), a)
    fmt.Printf("b 长度%v 容量%v 值%v \n", len(b), cap(b), b)

}

func main() {
    copySlice()
}
```

![](/assets/import86.png)

### copy\(\)函数 {#_5-2-copy-函数}

* Go 语言内建的 copy\(\)函数可以迅速地将一个切片的数据复制到另外一个切片空间中

* copy\(\)函数的使用格式如下： copy\(destSlice, srcSlice \[\]T\)

* 其中：

  * srcSlice: 数据来源切片
  * destSlice: 目标切片

```go
package main

import "fmt"

func deepcopySlice() {
    a := []int{1, 2, 3, 4}
    fmt.Printf("长度%v 容量%v 值%v \n", len(a), cap(a), a)
    b := []int{5, 6, 7, 8}
    fmt.Printf("长度%v 容量%v 值%v \n", len(b), cap(b), b)
    copy(b, a)
    fmt.Printf("a 长度%v 容量%v 值%v \n", len(a), cap(a), a)
    fmt.Printf("b 长度%v 容量%v 值%v \n", len(b), cap(b), b)
    b[0] = 789
    fmt.Printf("赋值后a 长度%v 容量%v 值%v \n", len(a), cap(a), a)
    fmt.Printf("赋值后b 长度%v 容量%v 值%v \n", len(b), cap(b), b)
}

func main() {
    deepcopySlice()
}
```

![](/assets/import87.png)

## sort\(\) {#_06-sort}

### 正序排序 {#_6-1-正序排序}

* 对于 int 、 float64 和 string 数组或是切片的排序
* go 分别提供了 sort.Ints\(\) 、sort.Float64s\(\) 和 sort.Strings\(\) 函数， 默认都是从小到大排序

```go
package main

import (
    "fmt"
    "sort"
)

func sortSlice() {
    aSlice := []int{3, 1, 5, 2, 8}
    sort.Ints(aSlice)
    fmt.Println(aSlice)
    bSlice := []string{"a", "c", "d", "b"}
    sort.Strings(bSlice)
    fmt.Println(bSlice)
}

func main() {
    sortSlice()

}
```

![](/assets/import88.png)

### sort 降序排序 {#_6-2-sort-降序排序}

* Golang的sort 包 可 以 使 用 sort.Reverse\(slice\) 来 调 换slice.Interface.Less
* 也就是比较函数，所以， int 、 float64 和 string的逆序排序函数可以这么写

```go
package main

import (
    "fmt"
    "sort"
)

func reserveSortSlice() {
    aSlice := []int{3, 1, 5, 2, 8}
    sort.Sort(sort.Reverse(sort.IntSlice(aSlice)))
    fmt.Println(aSlice)
    bSlice := []string{"a", "c", "d", "b"}
    sort.Sort(sort.Reverse(sort.StringSlice(bSlice)))
    fmt.Println(bSlice)
}

func main() {
    reserveSortSlice()
}
```

![](/assets/import89.png)

