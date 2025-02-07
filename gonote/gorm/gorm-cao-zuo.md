# GORM操作

## GORM介绍

### GORM是什么

- GORM 是 golang 的一个 orm 框架，它是一个单独的 ORM 框架。
- 相比 beego 自带的 orm 框架，语法要更友好一些，关联查询更简单、功能更强大一些。
- 简单说，ORM 就是通过实例对象的语法，完成关系型数据库的操作的技术
- 是"对象-关系 映射"（Object/Relational Mapping） 的缩写

### GORM功能介绍

[Gorm 官方文档](https://gorm.io/zh_CN/docs/query.html)

- 全功能 ORM (无限接近)
- 关联 (Has One, Has Many, Belongs To, Many To Many, 多态)
- 钩子 (在创建/保存/更新/删除/查找之前或之后)
- 预加载
- 事务
- 复合主键
- SQL 生成器
- 数据库自动迁移
- 自定义日志
- 可扩展性, 可基于 GORM 回调编写插件
- 所有功能都被测试覆盖
- 开发者友好

### 创建一个项目

```go
bee new beegogorm
go mod init beegogorm
go build -mod=mod
```

## GORM基本使用

### 安装gorm

```go
go get -u github.com/jinzhu/gorm
```

### 建立数据库链接

- `models/core.go`

```go
package models
import (
	"github.com/astaxie/beego"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

var DB *gorm.DB
var err error

func init() {
	//和数据库建立连接
	DB, err = gorm.Open("mysql", "root:123456@/beego?charset=utf8&parseTime=True&loc=Local")
	if err != nil {
		beego.Error()
	}
}
```

### 关闭数据库链接

```go
package main
import (
	"beegogorm/models"
	_ "beegogorm/routers"

	"github.com/astaxie/beego"
)

func main() {
	beego.Run()
	defer models.DB.Close() //关闭数据库连接
}
```

### 定义数据库模型

- `models/user.go`

```go
package models

type User struct {
	Id       int
	Username string
	Age      int
	Email    string
	AddTime  int
}

//定义结构体操作的数据库表
func (User) TableName() string {
	return "user"
}
```

### 自动创建表

- 注意：GORM 的AutoMigrate函数，仅支持建表，不支持修改字段和删除字段，避免意外导致丢失数据。
- [GORM更多用法](https://www.tizi365.com/archives/982.html)

```go
func init() {
	//和数据库建立连接
	DB, err = gorm.Open("mysql", "root:chnsys@2016@/beegodb?charset=utf8&parseTime=True&loc=Local")
	if err != nil {
		beego.Error()
	}

	if !DB.HasTable(&User{}){
		// 创建表
		DB.CreateTable(&User{})     // 根据User结构体建表
		DB.Set("gorm:table_options", "ENGINE=InnoDB").CreateTable(&User{})  // 设置表结构的存储引擎为InnoDB
	}
}
```

## GORM增删改查

### 基本增删改查

- `controllers/user.go`

```go
package controllers

import (
	"beegogorm/models"
	"github.com/astaxie/beego"
	"time"
)

type UserController struct {
	beego.Controller
}

func (c *UserController) UserAdd() {        // 1.增
	user := models.User{
		Username: "zhangsan",
		Age:      26,
		Email:    "zhangsan.qq.com",
		AddTime:  int(time.Now().Unix()),
	}
	models.DB.Create(&user)
	c.Ctx.WriteString("增加数据成功")
}

func (c *UserController) UserDelete() {      // 2.删
	user := models.User{Id: 1}
	models.DB.Delete(&user)
	c.Ctx.WriteString("删除数据成功")
}

func (c *UserController) UserEdit() {       // 3.改
	//1、查找id=5的数据
	user := models.User{Id: 5}
	//models.DB.First(&user)

	//2、执行修改
	user.Username = "王五"
	models.DB.Save(&user)

	c.Ctx.WriteString("修改数据成功")
}

func (c *UserController) UserSelect() {      // 4.查
	//1、查询一条数据
	// user := models.User{Username: "lisi"}
	// models.DB.Find(&user)

	//2、查询所有数据
	user := []models.User{}
	models.DB.Find(&user)
	c.Data["json"] = user
	c.ServeJSON()
}
```

### 定义路由

```go
package routers
import (
	"beegogorm/controllers"
	"github.com/astaxie/beego"
)

func init() {
    beego.Router("/user/add/", &controllers.UserController{},"get:UserAdd")
    beego.Router("/user/delete/", &controllers.UserController{},"get:UserDelete")
    beego.Router("/user/edit/", &controllers.UserController{},"get:UserEdit")
    beego.Router("/user/select/", &controllers.UserController{},"get:UserSelect")
}
```