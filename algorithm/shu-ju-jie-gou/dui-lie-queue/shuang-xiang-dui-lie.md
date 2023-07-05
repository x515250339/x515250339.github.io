# 双向队列

python 内置模块，超出大小，顶出第一个，容量为3， 【0,1,2】，append(3)，【1,2,3】

```
from collections import deque

q = deque()
q.append(1)
print(q.popleft())

q.appendleft(2)
print(q.pop())
```
