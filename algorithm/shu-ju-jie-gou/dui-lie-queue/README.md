# 队列(Queue)

### 定义

* 队列是一个数据集合，仅允许在列表的一端进行插入，另一端进行删除
* 插入的一端称为队尾（rear），插入动作叫进队或入队 O(1)
* 进行删除的一端称为对头（front），删除动作称为出队 O(1)
* 队列性质：先进先出（First-in, First-out）
* 双向队列：队列的两端都允许进行进队和出队操作

<figure><img src="../../.gitbook/assets/test7.gif" alt=""><figcaption></figcaption></figure>

### 利用python包-队列使用方法

```python
from queue import Queue
#1. 基本FIFO队列  先进先出 FIFO即First in First Out,先进先出
#2. maxsize设置队列中，数据上限，小于或等于0则不限制，容器中大于这个数则阻塞，直到队列中的数据被消掉
q = Queue(maxsize=0)

#3. 写入队列数据
q.put(0)
q.put(1)
q.put(2)

#4. 输出当前队列所有数据
print(q.queue)

#5. 删除队列数据，并返回该数据
q.get()

#6. 输也所有队列数据
print(q.queue)
```

### 手写队列

```python
class Queue:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop(0)

    def is_empty(self) -> bool:
        return not bool(self.q)

    def size(self) -> int:
        return len(self.q)


if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.pop())
    print(q.is_empty())
    print(q.size())
```

### 队列应用场景

* 1.队列主要的功能是在多个进程间共享数据，实现业务解耦，提高效率
* 2.生产者线程只需要把任务放入队列中，消费者线程只需要到队列中取数据进行处理
* 注：队列与列表区别
  * 列表中数据虽然是排列的，但数据被取走后还会保留，而`队列中这个容器的数据被取后将不会保留`
