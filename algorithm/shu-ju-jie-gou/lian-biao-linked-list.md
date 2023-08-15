# 链表(Linked List)

### 单链表定义

* 注：链表中每个元素都是一个对象，每个对象称为一个节点
* 每个节点包含两部分：
  * `数据域`： 存放当前节点数据
  * `指针域`： 指向下一个节点的内存地址

插入演示

<figure><img src="../.gitbook/assets/test9.gif" alt=""><figcaption></figcaption></figure>

删除演示

<figure><img src="../.gitbook/assets/test10.gif" alt=""><figcaption></figcaption></figure>

### python模拟单链表

```python
class Linked:

    def __init__(self, item: int, next=None):
        self.item = item
        self.next = next


l = Linked(1, Linked(2, Linked(3, Linked(4))))

print(l)
print(l.item)
print(l.next.item)
print(l.next.next.item)
```

### 单向链表反转

```python
class Linked:

    def __init__(self, item: int, next: int = None):
        self.item = item
        self.next = next


def list_reverse(head=None):
    if head is None:
        return None
    L, R, cur = None, None, head  # 左指针 右指针 游标
    while cur.next is not None:
        L = R  # 左侧指针指向以前右侧指针位置
        R = cur  # 右侧指针前进一位指向当前游标位置
        cur = cur.next  # 游标每次向前进一位
        R.next = L  # 右侧指针指向左侧实现反转
    cur.next = R  # 当跳出 while 循环时 cur(原链表最后一个元素) R(原链表倒数第二个元素)
    return cur


'''
原始链表：1 -> 2 -> 3 -> 4
反转链表：4 -> 3 -> 2 -> 1
'''
L = Linked(1)
L.next = Linked(2)
L.next.next = Linked(3)
L.next.next.next = Linked(4)
print(L.item)
print(L.next.item)
print(L.next.next.item)
l = list_reverse(L)
print(l.item)
print(l.next.item)
print(l.next.next.item)

```

### 链表时间复杂度

* 从链表中取出一个元素，时间复杂度： `O(n)`
  * n代表列表长度
* 遍历链表： `O(N)`
* 删除一个链表中的元素：O(1)
