# interface面向对象

## Golang接口的定义

### Golang 中的接口

* 在Go语言中接口（interface）是一种类型，一种抽象的类型。
* 接口（interface）定义了一个对象的行为规范，只定义规范不实现，由具体的对象来实现规范的细节。
* 实现接口的条件
  * 一个对象只要全部实现了接口中的方法，那么就实现了这个接口。
  * 换句话说，接口就是一个需要实现的方法列表。

### 为什么要使用接口

* 上面的代码中定义了猫和狗，然后它们都会叫，你会发现main函数中明显有重复的代码
* 如果我们后续再加上猪、青蛙等动物的话，我们的代码还会一直重复下去
* 那我们能不能把它们当成“能叫的动物”来处理呢？

```go
package main
import (
    "fmt"
)

type Cat struct {
    Name string
}
func (c Cat) Say() string { return c.Name + "：喵喵喵" }

type Dog struct {
    Name string
}
func (d Dog) Say() string { return d.Name + ": 汪汪汪" }

func main() {
    c := Cat{Name: "小白猫"}    // 小白猫：喵喵喵
    fmt.Println(c.Say())
    d := Dog{"阿黄"}
    fmt.Println(d.Say())       // 阿黄: 汪汪汪
}
/*
小白猫：喵喵喵
阿黄: 汪汪汪
 */
```

### 定义一个Usber接口

* 定义一个 **Usber** 接口让 **Phone** 和 **Camera** 结构体实现这个接口

```go
package main

import "fmt"

//1.接口是一个规范
type Usber interface {
    start()
    stop()
}

//2.如果接口里面有方法的话，必要要通过结构体或者通过自定义类型实现这个接口
type Phone struct {
    Name string
}

//3.手机要实现usb接口的话必须得实现usb接口中的所有方法
func (p Phone) start() {
    fmt.Println(p.Name, "启动")
}
func (p Phone) stop() {
    fmt.Println(p.Name, "关机")
}

func main() {
    p := Phone{
        Name: "华为手机",
    }
    var p1 Usber   // golang中接口就是一个数据类型
    p1 = p       // 表示手机实现Usb接口
    p1.start()
    p1.stop()
}
/*
华为手机 启动
华为手机 关机
 */
```

### go中类

* Go语言中没有“类”的概念，也不支持“类”的继承等面向对象的概念。
* Go语言中通过结构体的内嵌再配合接口比面向对象具有更高的扩展性和灵活性。

## 空接口

### 空接口说明

* `golang中空接口也可以直接当做类型来使用，可以表示任意类型`
* Golang 中的接口可以不定义任何方法，没有定义任何方法的接口就是空接口。
* 空接口表示没有任何约束，因此任何类型变量都可以实现空接口。
* 空接口在实际项目中用的是非常多的，用空接口可以表示任意数据类型。

### 空接口作为函数的参数

```go
package main
import "fmt"

//空接口作为函数的参数
func show(a interface{}) {
    fmt.Printf("值:%v 类型:%T\n", a, a)
}
func main() {
    show(20)                      // 值:20 类型:int
    show("你好golang")            // 值:你好golang 类型:string
    slice := []int{1, 2, 34, 4}
    show(slice)                     // 值:[1 2 34 4] 类型:[]int
}
```

### 切片实现空接口

```go
package main
import "fmt"

func main() {
    var slice = []interface{}{"张三", 20, true, 32.2}
    fmt.Println(slice)  // [张三 20 true 32.2]
}
```

### map 的值实现空接口

```go
package main
import "fmt"

func main() {
    // 空接口作为 map 值
    var studentInfo = make(map[string]interface{})
    studentInfo["name"] = "张三"
    studentInfo["age"] = 18
    studentInfo["married"] = false
    fmt.Println(studentInfo)
    // [age:18 married:false name:张三]
}
```

## 类型断言

* 一个接口的值（简称接口值）是由一个具体类型和具体类型的值两部分组成的。
* 这两部分分别称为接口的动态类型和动态值。
* 如果我们想要判断空接口中值的类型，那么这个时候就可以使用类型断言
* 其语法格式：`x.(T)`
  * x : 表示类型为 interface{}的变量
  * T : 表示断言 x 可能是的类型

```go
package main
import "fmt"

func main() {
    var x interface{}
    x = "Hello golnag"
    v, ok := x.(string)
    if ok {
        fmt.Println(v)
    }else {
        fmt.Println("非字符串类型")
    }
}
```

## 值接收者和指针接收者

### 值接收者

* 当方法作用于值类型接收者时，Go语言会在代码运行时将接收者的值复制一份。
* 在值类型接收者的方法中可以获取接收者的成员值，但修改操作只是针对副本，无法修改接收者变量本身。

```go
package main
import "fmt"
type Usb interface {
    Start()
    Stop()
}
type Phone struct {
    Name string
}
func (p Phone) Start() {
    fmt.Println(p.Name, "开始工作")
}
func (p Phone) Stop() {
    fmt.Println("phone 停止")
}
func main() {
    phone1 := Phone{       // 一：实例化值类型
        Name: "小米手机",
    }
    var p1 Usb = phone1      //phone1 实现了 Usb 接口 phone1 是 Phone 类型
    p1.Start()

    phone2 := &Phone{         // 二：实例化指针类型
        Name: "苹果手机",
    }
    var p2 Usb = phone2      //phone2 实现了 Usb 接口 phone2 是 *Phone 类型
    p2.Start()            //苹果手机 开始工作
}
```

### 指针接收者

* 指针类型的接收者由一个结构体的指针组成
* 由于指针的特性，调用方法时修改接收者指针的任意成员变量，在方法结束后，修改都是有效的。
* 这种方式就十分接近于其他语言中面向对象中的`this`或者`self`。
* 例如我们为`Person`添加一个`SetAge`方法，来修改实例变量的年龄。

```go
package main
import "fmt"
type Usb interface {
    Start()
    Stop()
}
type Phone struct {
    Name string
}
func (p *Phone) Start() {
    fmt.Println(p.Name, "开始工作")
}
func (p *Phone) Stop() {
    fmt.Println("phone 停止")
}
func main() {
    /*错误写法
    phone1 := Phone{
        Name: "小米手机",
    }
    var p1 Usb = phone1
    p1.Start()
    */
    //正确写法
    phone2 := &Phone{     // 指针类型接收者只能传入指针类型，不能传入值类型
        Name: "苹果手机",
    }
    var p2 Usb = phone2 //phone2 实现了 Usb 接口 phone2 是 *Phone 类型
    p2.Start()
    //苹果手机 开始工作
}
```

### `值类型接收者`使用时机

* 1、需要修改接收者中的值
* 2、接收者是拷贝代价比较大的大对象
* 3、保证一致性，如果有某个方法使用了指针接收者，那么其他的方法也应该使用指针接收者。

## 一个结构体实现多个接口

* Golang 中一个结构体也可以实现多个接口

```go
package main
import "fmt"
type AInterface interface {
    GetInfo() string
}
type BInterface interface {
    SetInfo(string, int)
}
type People struct {
    Name string
    Age int
}
func (p People) GetInfo() string {
    return fmt.Sprintf("姓名:%v 年龄:%d", p.Name, p.Age)
}
func (p *People) SetInfo(name string, age int) {
    p.Name = name
    p.Age = age
}
func main() {
    var people = &People{
        Name: "张三",
        Age: 20,
    }
    // people 实现了 AInterface 和 BInterface
    var p1 AInterface = people
    var p2 BInterface = people
    fmt.Println(p1.GetInfo())
    p2.SetInfo("李四", 30)         // 姓名:张三 年龄:20
    fmt.Println(p1.GetInfo())      // 姓名:李四 年龄:30
}
```

## 接口嵌套\(`继承`\)

* 接口与接口间可以通过嵌套创造出新的接口。

```go
package main
import "fmt"
type SayInterface interface {
    say()
}
type MoveInterface interface {
    move()
}
// 接口嵌套
type Animal interface {
    SayInterface
    MoveInterface
}
type Cat struct {
    name string
}
func (c Cat) say() {
    fmt.Println("喵喵喵")
}
func (c Cat) move() {
    fmt.Println("猫会动")
}
func main() {
    var x Animal
    x = Cat{name: "花花"}
    x.move()    // 猫会动
    x.say()     // 喵喵喵
}
```



