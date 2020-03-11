# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 20:53
# @Author  : Jackey-lu
# @File    : 543. 二叉树的直径.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.count = 1
        def width(root):
            if not root: return 0
            left = width(root.left)
            right = width(root.right)
            self.count = max(self.count, left+right+1)
            return max(left, right)+1
        width(root)
        return self.count-1








class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            # 访问到空节点了，返回0
            if not node: return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L+R+1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1