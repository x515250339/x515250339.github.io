# 字符串

Go 语言里的字符串的内部实现使用 UTF-8 编码。  
字符串的值为双引号\("\)中的内容，可以在 Go 语言的源码中直接添加非 ASCII 码字符  
s1 := "hello"  
s2 := "你好"

# 字符串转义符

Go 语言的字符串常见转义符包含回车、换行、单双引号、制表符等

```go
package main

import (
    "fmt"
)

func main() {
    // 创建字符串
    fmt.Println("str := \"c:\\Code\\demo\\go.exe\"") // str := "c:\Code\demo\go.exe"
    str := "c:\\Code\\demo\\go.exe"
    fmt.Println("str := ", str)
}
```

# ![](/assets/import33.png)

# 多行字符串

反引号间换行将被作为字符串中的换行，但是所有的转义字符均无效，文本将会原样输出。

```go
package main

import (
    "fmt"
)

func main() {
    // 创建的多行字符串
    sManyLine := `第一行
第二行
第三行`
    fmt.Println(sManyLine)
}
```

# ![](/assets/import34.png)

# byte和rune

Go 语言的字符有以下两种  
uint8类型，或者叫 byte 型：代表了ASCII码的一个字符。  
rune类型：代表一个 UTF-8字符  
字符串底层是一个byte数组，所以可以和\[\]byte类型相互转换。  
字符串是不能修改的 字符串是由byte字节组成，所以字符串的长度是byte字节的长度。  
rune类型用来表示utf8字符，一个rune字符由一个或多个byte组成。

```go
package main

import (
    "fmt"
)

// byte和rune
func byteAndRune() {
    s := "日本垃垃"
    fmt.Println(s)
    sRune := []rune(s)
    fmt.Println("美国" + string(sRune[2:]))
}

func main() {
    byteAndRune()
}
```

# ![](/assets/import35.png)

# 字符串的常用操作

方法    介绍  
len\(str\)    求长度  
+或fmt.Sprintf    拼接字符串  
strings.Split    分割  
strings.Contains    判断是否包含  
strings.HasPrefix,strings.HasSuffix    前缀/后缀判断  
strings.Index\(\),strings.LastIndex\(\)    子串出现的位置  
strings.Join\(a\[\]string, sep string\)    join操作

# len\(str\)

```go
package main

import (
    "fmt"
)

// 获取字符串长度
func lenStr(a *string) {
    fmt.Println(len(*a))
}

func main() {
    var a = "string"
    lenStr(&a)

}
```

# ![](/assets/import36.png)

# +\(拼接\)

```go
package main

import (
    "fmt"
)

// 拼接字符串
func strJoin(a, b *string) {
    fmt.Println(*a + *b)
}

func main() {
    var a = "hi  "
    var b = "lao 8"
    strJoin(&a, &b)

}
```

# ![](/assets/import37.png)

# strings.Split\(\)

```go
package main

import (
    "fmt"
    "strings"
)

// 切分字符串
func strSplit(a *string) {
    bArr := strings.Split(*a, "/")
    fmt.Println(bArr)
    fmt.Println(bArr[0])
}

func main() {
    a := "123/456/789"
    strSplit(&a)
}
```

# strings.HasPrefix\(\)

首字符尾字母包含指定字符

```go
package main

import (
    "fmt"
    "strings"
)


func strHasPrefix(a *string) {
    // 是否以test开头
    if strings.HasPrefix(*a, "test") {
        fmt.Println("是test开头")
    } else if strings.HasSuffix(*a, "end") { //是否以en结尾
        fmt.Println("是end结尾")
    }
}

func main() {
    a := "test_a"
    strHasPrefix(&a)
    a = "a_end"
    strHasPrefix(&a)
}
```

# ![](/assets/import38.png)

# strings.Index\(\)

判断字符串出现的位置

```go
package main

import (
    "fmt"
    "strings"
)

// 判断字符串出现的位置
func indexStr(a *string) {
    index := strings.Index(*a, "w")
    fmt.Println(index)
}

func main() {
    // 判断字符串出现的位置
    a := "teswt"
    indexStr(&a)
}
```

# ![](/assets/import39.png)

# strings.Join\(\)

```go
package main

import (
    "fmt"
    "strings"
)

// 拼接字符串
func strJoin2(a *string) {
    aArr := strings.Split(*a, " ")
    fmt.Println(aArr)
    aStr := strings.Join(aArr, "-")
    fmt.Println(aStr)
}

func main() {
    var b = "lao 8"
    strJoin2(&b)
}
```

# ![](/assets/import40.png)

# 单引号

组成每个字符串的元素叫做“字符”，可以通过遍历字符串元素获得字符，字符用单引号（’）  
uint8 类型，或者叫 byte 型，代表了 ASCII 码的一个字符  
rune 类型，代表一个 UTF-8 字符

```go
package main

import (
    "fmt"
    "strings"
)

func strASCII() {
    a := 'a'
    name := "张三"
    // 当我们直接输出 byte（字符）的时候输出的是这个字符对应的码
    fmt.Println(a) // 97 这里输出的是 a 字符串的 ASCII值
    fmt.Println(name)
    // 如果我们要输出这个字符，需要格式化输出
    fmt.Printf("%c\n", a)
    // 或者声明并强转为str
    var b = string('a')
    fmt.Println(b)
}

func main() {
    // 单引号
    strASCII()
}
```

# ![](/assets/import41.png)

# 遍历字符串

```go
package main

import "fmt"

func main() {
    s := "hello word"
    // 通过下标去获取元素
    for i := 0; i < len(s); i++ {
        //%v 相应值的默认格式; %c 输出单个字符
        fmt.Printf("%v(%c)   ", s[i], s[i])
    }
    fmt.Println()
    // 遍历循环元素
    for _, j := range s {
        fmt.Printf("%v(%c)   ", j, j)
    }

}
```

# ![](/assets/import32.png)

# 修改字符串

要修改字符串，需要先将其转换成\[\]rune 或\[\]byte，完成后再转换为 string。  
无论哪种转换，都会重新分配内存，并复制字节数组。

```go
package main

import "fmt"

func main() {
    // 修改字符串，需要先将其转换成[]rune 或[]byte，完成后再转换为 string
    s1 := "big"
    byteS1 := []byte(s1)
    byteS1[0] = 'B'
    fmt.Println(string(byteS1))

    s2 := "Big"
    byteS2 := []rune(s2)
    byteS2[0] = 'b'
    fmt.Println(string(byteS2))
}
package main

import "fmt"

func main() {
    // 修改字符串，需要先将其转换成[]rune 或[]byte，完成后再转换为 string
    s1 := "big"
    byteS1 := []byte(s1)
    byteS1[0] = 'B'
    fmt.Println(string(byteS1))

    s2 := "Big"
    byteS2 := []rune(s2)
    byteS2[0] = 'b'
    fmt.Println(string(byteS2))
}
```

# ![](/assets/import43.png)

# sprintf转string

注意：sprintf 使用中需要注意转换的格式  
int 为%d  
float 为%f  
bool 为%t  
byte 为%c

```go
package main

import "fmt"

func main() {
    var i int = 10
    var f float64 = 2.00
    var t bool = true
    var b byte = 'a'
    var str string

    str = fmt.Sprintf("%d", i)
    fmt.Printf("类型: %T，值: %v \n", str, str)

    str = fmt.Sprintf("%f", f)
    fmt.Printf("类型: %T，值: %v \n", str, str)

    str = fmt.Sprintf("%t", t)
    fmt.Printf("类型: %T，值: %v \n", str, str)

    str = fmt.Sprintf("%c", b)
    fmt.Printf("类型: %T，值: %v \n", str, str)
}
```

# ![](/assets/import44.png)

# strconv

```go
package main

import (
    "fmt"
    "strconv"
)

func main() {
    // int 转换为 string
    var i int
    fmt.Printf("转换前类型：%T，值：%v \n", i, i)
    s1 := strconv.Itoa(i)
    fmt.Printf("转换后类型：%T，值：%v \n", s1, s1)
    fmt.Println()

    // float 转 string
    var i2 float64 = 0.01
    fmt.Printf("转换前类型：%T，值：%v \n", i2, i2)
    /* 参数 1：要转换的值
    参数 2：格式化类型
    参数 3: 保留的小数点 -1（不对小数点格式化）
    参数 4：格式化的类型
    */
    s2 := strconv.FormatFloat(i2, 'f', 2, 64)
    fmt.Printf("转换后类型：%T，值：%v \n", s2, s2)
    fmt.Println()

    // bool 转 string
    b := false
    fmt.Printf("转换前类型：%T，值：%v \n", b, b)
    s3 := strconv.FormatBool(b)
    fmt.Printf("转换后类型：%T，值：%v \n", s3, s3)
    fmt.Println()

    // int64 转 string
    var i3 int64 = 998
    fmt.Printf("转换前类型：%T，值：%v \n", i3, i3)
    var s4 = strconv.FormatInt(i3, 10)
    fmt.Printf("转换后类型：%T，值：%v \n", s4, s4)
    fmt.Println()

}
```

# ![](/assets/import46.png)

# string转int

```go
package main

import (
    "fmt"
    "strconv"
)

// string转int
func str2int2() {
    var a string = "1234"
    i64, _ := strconv.ParseInt(a, 10, 64)
    fmt.Printf("转换前类型: %T 转换后类型: %T 值: %v \n", a, i64, i64)
}

func main() {
    str2int2()
}
```

# ![](/assets/import47.png)

# string转float

```go
package main

import (
    "fmt"
    "strconv"
)

// string转float
func str2float() {
    var a string = "3.14"
    f32, _ := strconv.ParseFloat(a, 32)
    f64, _ := strconv.ParseFloat(a, 64)
    fmt.Printf("转换前类型: %T 转换后类型: %T 值: %v \n", a, f32, f32)
    fmt.Printf("转换前类型: %T 转换后类型: %T 值: %v \n", a, f64, f64)
}

func main() {
    str2float()
}
```

# ![](/assets/import48.png)

# string转bool

```go
package main

import (
    "fmt"
    "strconv"
)

// string转bool
func str2bool() {
    var a string = "true"
    b, _ := strconv.ParseBool(a)
    fmt.Printf("转换前类型: %T 转换后类型: %T 值: %v \n", a, b, b)
}

func main() {
    str2bool()
}
```

# ![](/assets/import49.png)

# string转字符

```go
package main

import (
    "fmt"
    "strconv"
)

// string转字符
func str2ASCII() {
    var a string = "hello goland"
    for _, i := range a {
        fmt.Printf("%v(%c)  ", i, i)
    }
}

func main() {
    str2ASCII()
}
```

![](/assets/import50.png)

# 字符串反转

```go
package main

import (
    "fmt"
    "strconv"
)

// 字符串反转
func strServer() {
    a := "test"
    r := []rune(a)
    for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    fmt.Printf(string(r))
}

func main() {
    strServer()
}
```

![](/assets/import51.png)

