# 栈(Stack)

### **定义**

栈是一个数据集合，可以理解为只能在一端进行插入或删除操作的列表。

特点：后进先出 （last-in, first-out）

概念：栈顶、栈底

栈的基本操作：

* 进栈 push O(1)
* 出栈 pop O(1)
* 取栈顶 gettop O(1)

进栈

<figure><img src="../../.gitbook/assets/test3.gif" alt=""><figcaption></figcaption></figure>

出栈

<figure><img src="../../.gitbook/assets/test4.gif" alt=""><figcaption></figcaption></figure>

### python实现

```python
class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        入栈
        :param item:
        :return:
        """
        self.stack.append(item)

    def get_top(self):
        """
        获取栈顶元素
        :return:
        """
        return self.stack[-1]

    def pop(self):
        """
        出栈
        :return:
        """
        return self.stack.pop()


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.stack)
    print(s.get_top())
    print(s.pop())
    print(s.get_top())
```

### 添加一些功能

```python
"""
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
"""


class Stack():
    """创建一个新的空栈类"""

    def __init__(self):
        """创建一个新的空栈"""
        self.alist = []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.alist.append(item)

    def pop(self):
        """弹出栈顶元素"""
        if self.alist == []:
            return None
        else:
            return self.alist.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.alist == []:
            return None
        else:
            return self.alist[-1]

    def is_empty(self):
        """判断栈是否为空"""
        return self.alist == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.alist)


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    print(s.size())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s.size())
    print(s.pop())
    print(s.size())
    print(s.is_empty())
    print(s.peek())

```

### 进阶写法 数字转二进制

```python
class MyStack:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        return self.s.pop()

    def size(self) -> int:
        return len(self.s)

    def empty(self) -> bool:
        return not bool(self.s)


stack = MyStack()


def trans_from(num: int) -> str:
    while num != 0:
        re_main = num % 2
        print("re_main", re_main)
        num = int(num / 2)
        print("num", num)
        stack.push(re_main)
    s = ""
    while not stack.empty():
        s += str(stack.pop())
    return s


if __name__ == '__main__':
    print(trans_from(12))

```
