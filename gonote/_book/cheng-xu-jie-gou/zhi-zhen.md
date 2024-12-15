# 指针

1.一个指针的值是另一个变量的地址,指针名字为p，那么可以说“p指针指向变量x”，或者说“p指针保存了x变量的内存地址”  
2.聚合类型每个成员,可以被取地址  
3.函数返回局部变量的地址也是安全的  
4.将指针作为参数调用函数，那将可以在函数中通过该指针来更新变量的值。  
5.我们对一个变量取地址，或者复制指针，我们都是为原变量创建了新的别名  
6.指针是实现标准库中flag包的关键技术，它使用命令行参数来设置对应变量的值

# demo

```go
/*
&是“取地址运算符”，是从一个变量获取地址
*是“解引用运算符”，可以简单理解为“从地址取值”， 是&的逆运算
你 testd 是一个 Test*类型，也就是指向 Test 的指针
然后&testd 就是 testd 变量本身的地址，类型应该是 Test 的指针的指针
*/

package main

import "fmt"

type Test struct {
    name string
}

func main() {
    var a int = 20 /* 声明实际变量 */
    var ip *int    /* 声明指针变量 */

    ip = &a /* 指针变量的存储地址 */

    fmt.Printf("a 变量的地址是: %x\n", &a)

    /* 指针变量的存储地址 */
    fmt.Printf("ip 变量储存的指针地址: %x\n", ip)

    /* 使用指针访问值 */
    fmt.Printf("*ip 变量的值: %d\n", *ip)
    main2()
}

func main2() {
    testa := Test{"test"}
    fmt.Println(testa)
    //结果{test}

    testb := &Test{"test"}
    fmt.Println(testb)
    //结果 &{test}

    testc := &Test{"test"}
    fmt.Println(*testc)
    //结果 {test}

    testd := &Test{"test"}
    fmt.Println(&testd)
    //结果 0xc000006030

    var a int = 1
    fmt.Println(a)
    //结果 1
    fmt.Println(&a)
    //结果 0xc00000c0d8
}
```

# new函数

1. 另一个创建变量的方法是调用用内建的new函数,new\(T\)将创建一个T类型的匿名变量，初始化为T类型的零值，然后返回变量地址，返回的指针类型为\*T。
2. 用new创建变量和普通变量声明语句方式创建变量没有什么区别，除了不需要声明一个临时变量的名字外，我们还可以在表达式中使用new\(T\)。换言之，new函数类似是一种语法糖，而不是一个新的基础概念。
   ```go
   p := new(int)   // p, *int 类型, 指向匿名的 int 变量
   fmt.Println(*p) // "0"
   *p = 2          // 设置 int 匿名变量的值为 2
   fmt.Println(*p) // "2"
   ```



