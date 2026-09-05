# LC100 相同的树 - 迭代版（栈 + 列表）本地可跑版

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        stack = [(p, q)] # 中括号套小括号：列表里装一个"节点对"元组
        while stack:
            a, b = stack.pop()
            if a is None and b is None:
                continue               # 这对都空，没事，跳过
            if a is None or b is None:
                return False # 一空一不空 → 否决
            if a.val != b.val:
                return False           # 值不等 → 否决
            stack.append((a.left, b.left)) # 左右孩子成对压栈
            stack.append((a.right, b.right))
        return True                    # 栈空了都没错 → 全相同

# ============ 以下是测试代码 ============
if __name__ == "__main__":
    sol = Solution()

    # 两棵相同的 [1,2,3]
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print("相同树:", sol.isSameTree(t1, t2))         # 应 True

    # 结构不同 [1,2]  [1,None,2]
    t3 = TreeNode(1, TreeNode(2))
    t4 = TreeNode(1, None, TreeNode(2))
    print("结构不同:", sol.isSameTree(t3, t4)) # 应 False

    # 两棵空树
    print("两空:", sol.isSameTree(None, None))        # 应 True

    # 一空一不空
    print("一空:", sol.isSameTree(None, TreeNode(1))) # 应 False

    # 值不等 [1,2,3]  [1,2,4]
    t5 = TreeNode(1, TreeNode(2), TreeNode(3))
    t6 = TreeNode(1, TreeNode(2), TreeNode(4))
    print("值不等:", sol.isSameTree(t5, t6))          # 应 False
