选择排序: 通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。 **算法描述** 快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：

- 从数列中挑出一个元素，称为 “基准”（pivot）；
- 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
- 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

时间复杂度 `O(n log n)`

空间复杂度 `O(1)`

```python
import random


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        # 从右面找比 tmp 小的值
        while left < right and li[right] >= tmp:
            # 往前走一步
            right -= 1
        # 把右边的值写道左边的空位上
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        # 把左边的值写到右边的空位上
        li[right] = li[left]
    # 把 tmp 归位
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    """
    快速排序 时间复杂度O(n log n)  空间复杂度O(1)
    :param li:
    :param left:
    :param right:
    :return:
    """
    # 至少两个元素
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = list(range(10000))
random.shuffle(li)
quick_sort(li, 0, len(li) - 1)
print(li)
```

![快速排序](kuai-supai-xu-ff08-quick-sort.assets/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F.gif)