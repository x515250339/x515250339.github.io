# 数组(Array)

**定义**：数组（Array）是一种线性表数据结构。它用一组连续的内存空间，来存储一组具有相同类型的数据。

**python列表定义**：支持存储多种数据类型，内存地址不是连续的。



数组：因为数据类型相同，存储的是连续的内存空间

* 查找：O(1)
* 插入：O(n)
* 删除：O(n)

插入演示

<figure><img src="../.gitbook/assets/test1 (1).gif" alt=""><figcaption></figcaption></figure>

删除演示

<figure><img src="../.gitbook/assets/test2.gif" alt=""><figcaption></figcaption></figure>



python列表：因为数据类型相同，存储的是连续的内存空间

* 查找：O(n)
* 插入：O(n)
* 删除：O(1)



python 实现 Array

```python
import array

# 创建一个存储整型的array
arr1 = array.array('i', [1, 2, 3, 4, 5, 6])
arr2 = array.array('f', [1, 2, 3, 4, 5, 6])
arr3 = array.array('u', [u'a', u'b', u'c'])
print(arr1)
print(arr2)
print(arr3)
```
