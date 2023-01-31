归并排序：归并排序是建立在归并操作上的一种有效，稳定的排序算法，该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。

作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：

1.自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
2.自下而上的迭代；

时间复杂度 `O(n log n)`

空间复杂度 `O(n)`

```python
def merge(data, low, mid, high):
    i = low
    j = mid + 1
    tmp = []

    while i <= mid and j <= high:  # 只要左右两边都有数
        if data[i] < data[j]:
            tmp.append(data[i])
            i += 1
        else:
            tmp.append(data[j])
            j += 1
    # while 执行完后，肯定有一部分没数
    while i <= mid:
        tmp.append(data[i])
        i += 1
    while j <= high:
        tmp.append(data[j])
        j += 1
    # 交换值
    data[low: high + 1] = tmp


def merge_sort(data, low, high):
    if low < high:  # 保证至少有两个元素，递归
        mid = (low + high) // 2
        merge_sort(data, low, mid)
        merge_sort(data, mid + 1, high)
        merge(data, low, mid, high)


import random

data = [i for i in range(10)]
random.shuffle(data)
print(data)
merge_sort(data, 0, len(data) - 1)
print(data)
```

![归并排序](gui-bing-pai-xu-ff08-merge-sort.assets/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F.gif)