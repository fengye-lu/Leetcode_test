# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 18:14
# @Author  : Jackey-lu
# @File    : 225. 用队列实现栈.py

# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 18:14
# @Author  : Jackey-lu
# @File    : 225. 用队列实现栈.py

import queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = queue.LifoQueue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.d.put(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        rel = self.d.get()
        return rel


    def top(self) -> int:
        """
        Get the top element.
        """
        rel = self.d.get()
        self.d.put(rel)
        return rel


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.d.empty()



# class MyStack:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.q = []
#
#     def push(self, x: int) -> None:
#         """
#         Push element x onto stack.
#         """
#         self.q.append(x)
#         q_length = len(self.q)
#         while q_length > 1:
#             self.q.append(self.q.pop(0)) #反转前n-1个元素，栈顶元素始终保留在队首
#             q_length -= 1
#
#     def pop(self) -> int:
#         """
#         Removes the element on top of the stack and returns that element.
#         """
#         return self.q.pop(0)
#
#     def top(self) -> int:
#         """
#         Get the top element.
#         """
#         return self.q[0]
#
#
#     def empty(self) -> bool:
#         """
#         Returns whether the stack is empty.
#         """
#         return not bool(self.q)








# Your MyStack object will be instantiated and called as such:
obj = MyStack()
# obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
param_4 = obj.empty()
print(param_4)