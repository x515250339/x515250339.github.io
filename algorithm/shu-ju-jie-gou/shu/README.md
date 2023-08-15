# 树

### 树的概念

#### 树的特性

* 1）一棵树中的任意两个结点有且仅有唯一的一条路径连通；
* 2）一棵树如果有n个结点，则它一定有n−1条边；
* 3）在一棵树中加一条边将会构成一个回路。

#### 二叉树

* 1）二叉树是一种特殊的树，二叉树的特点是每个结点最多有两个儿子。
* 2）二叉树使用范围最广，一颗多叉树也可以转化为二叉树。

#### 满二叉树

* 1）二叉树中每个内部节点都有两个儿子，满二叉树所有的叶节点都有相同的深度。
* 2）满二叉树是一棵深度为h且有2h−1个结点的二叉树。

#### 完全二叉树

* 1）若设二叉树的高度为h，除了第h层外，其他层的结点数都达到最大个数，第h层从右向左连续 缺若干个结点，则为完全二叉树。

#### 树的特点

* 1、如果一棵完全二叉树的父节点编号为K,则其左儿子的编号是2K,右儿子的结点编号为2K+1
* 2、已知完全二叉树的总节点数为n求叶子节点个数：
  * 当n为奇数时：（n+1）/2
  * 当n为偶数时 : （n）/2
* 3、已知完全二叉树的总节点数为n求父节点个数：为：n/2
* 4、已知完全二叉树的总节点数为n求叶子节点为2的父节点个数：
  * 当n为奇数时：n/2
  * 当n为偶数时 : n/2-1
* 5、如果一棵完全二叉树有N个结点，那么这棵二叉树的深度为【log2（N+1）log2（N+1）】（向上取整）

### 二叉树基本操作

#### 数遍历说明

* **1. 前序遍历：** DBACEGF（根节点排最先，然后同级先左后右）
* **2. 中序遍历：** ABCDEFG (先左后根最后右）
* **3. 后序遍历：** ACBFGED （先左后右最后根）

#### 生成树结构

```python
class Tree:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left  # 左子树
        self.right = right  # 右子树


# 生成树
T = Tree("D", Tree("B", Tree("A"), Tree("C")), Tree("E", right=Tree("G", Tree("F"))))
"""
            D
            /\
           B  E
           /\  \
          A  C  G
                /
               F
"""
```

#### 前序遍历

**前序遍历**

```python
def pre_traverse(tree):
    """
    前序遍历 根 左 右（根节点排最先，然后同级先左后右）
    :param tree: 二叉树
    :return:
    """
    if tree is None:
        return
    print(tree.value)
    pre_traverse(tree.left)
    pre_traverse(tree.right)


print("前序遍历")
pre_traverse(T)
```

**前序遍历步骤推演**

```python
前序排列原理：
#####此时执行preTraverse(root.left) 函数
'''
1、第一步 root=Node(D) print D，D入栈[D]
2、第二步 root=Node(D).left=Node(B) print B, B入栈[D,B]
3、第三步 root=Node(B).left=Node(A) print A, A入栈[D,B,A]
4、第四步 root=Node(A).left=None,没有进入递归，顺序执行preTraverse(root.right)
5、第五步 Node(A).right==None，也没有进入递归，此时preTraverse(A) 函数才会正真返回，A出栈[D,B]
6、第六步 A的上级调用函数为：preTraverse(B.left),所以接着会顺序执行preTraverse(B.right),B的左右节点访问后B出栈[D]
7、第七步 Node(B).right==Node(C) print C,C入栈[D,C]
8、第八步 Node(C).left==None, Node(C).right==None,访问完C的左右节点后函数返回C出栈，返回上级调用[D]
9、第九步 此时返回上级调用执行preTraverse(D.right)=Node(E) print E,D出栈，E入栈[E] 
'''

'''此时输出结果：DBACE'''
```

#### 中序遍历

```python
def mid_traverse(tree):
    """
    中序遍历 左根右（先左 后根 最后右）
    :param tree:
    :return:
    """
    if tree is None:
        return
    mid_traverse(tree.left)
    print(tree.value)
    mid_traverse(tree.right)


print("中序遍历")
mid_traverse(T)
```

#### 后序遍历

```python
def after_traverse(tree):
    """
    后序遍历 左右根（先左 后右 最后根）
    :param tree:
    :return:
    """
    if tree is None:
        return
    after_traverse(tree.left)
    after_traverse(tree.right)
    print(tree.value)


print("后序遍历")
after_traverse(T)
```

#### 分层打印二叉树

```python
def layered_print(tree):
    """
    分层打印二叉树
    :param tree:
    :return:
    """
    if not tree:
        return
    cur_layer = [tree]
    while cur_layer:
        layer_value = []
        next_layer = []
        for t in cur_layer:
            layer_value.append(t.value)
            if t.left:
                next_layer.append(t.left)
            if t.right:
                next_layer.append(t.right)
        print(layer_value)
        cur_layer = next_layer


print("分层打印")
layered_print(T)
```
