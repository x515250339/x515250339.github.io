堆排序：利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。 **算法描述** - 将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区； - 将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]； - 由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。

大根堆：根最大

小根堆：根最小

时间复杂度 `O(n log n)`

空间复杂度 `O(1)`

```python
import random


def sift(data_list, low, high):
    """

    :param data_list: 列表
    :param low: 堆的根节点
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # 指向根结点
    j = 2 * i + 1  # 左孩子
    tmp = data_list[low]  # 存放堆顶

    while j <= high:  # 只要左有数
        if j + 1 <= high and data_list[j + 1] > data_list[j]:  # 如果右孩子有数并且比较大
            j += 1  # 指向右孩子
        if data_list[j] > tmp:
            data_list[i] = data_list[j]
            i = j  # 往下一层
            j = 2 * i + 1
        else:  # tmp 更大，把tmp放到i的位置上
            data_list[i] = tmp  # 把 tmp 放到某一级领导上
            break
    data_list[i] = tmp  # 把 tmp 放到叶子节点上


def heap_sort(data_list):
    n = len(data_list)
    for i in range((n - 2) // 2, -1, -1):
        # i 表示建堆的时候调整的部分的根的下标
        sift(data_list, i, n - 1)
    # 堆建立完成
    for i in range(n - 1, -1, -1):
        # i 指向当前堆的最后一个元素
        data_list[0], data_list[i] = data_list[i], data_list[0]
        sift(data_list, 0, i - 1)  # i - 1是新的high


data = [random.randint(1, 100) for i in range(10)]
print(data)
heap_sort(data)
print(data)
```

<video src="C:/Users/51525/Downloads/%E5%A0%86%E6%8E%92%E5%BA%8F.mp4"></video>