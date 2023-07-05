# 哈希表

### 哈希表

* `注：`字典类型是Python中最常用的数据类型之一，它是一个键值对的集合，字典通过键来索引，关联到相对的值，理论上它的查询复杂度是 O(1)

#### 哈希表 (hash tables)

* 1.哈希表（也叫散列表），根据关键值对(Key-value)而直接进行访问的数据结构。
* 2.它通过把key和value映射到表中一个位置来访问记录，这种查询速度非常快，更新也快。
* 3.而这个映射函数叫做哈希函数，存放值的数组叫做哈希表。
* 4.通过把每个对象的关键字k作为自变量，通过一个哈希函数h(k)，将k映射到下标h(k)处，并将此对象存储在这个位置。

#### 具体操作过程

* 1.数据添加：
  * 把key通过哈希函数转换成一个整型数字，然后就将该数字对数组长度进行取余
  * 取余结果就当作数组的下标，将value存储在以该数字为下标的数组空间里。
* 2.数据查询：再次使用哈希函数将key转换为对应的数组下标，并定位到数组的位置获取value。

### 字典如何存储的呢?

* 1.比如字典`{“name”:”zhangsan”,”age”:26}`，那么他们的字典key为name、age，假如哈希函数h(“name”)=1、h(“age”)=3,
* 2.那么对应字典的key就会存储在列表对应下标的位置，\[None,“zhangsan”,None,26]

### 解决hash冲突

<figure><img src="../.gitbook/assets/test7.png" alt=""><figcaption></figcaption></figure>

### python字典操作时间复杂度

<figure><img src="../.gitbook/assets/test6.png" alt=""><figcaption></figcaption></figure>
