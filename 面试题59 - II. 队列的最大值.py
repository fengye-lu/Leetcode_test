# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 19:42
# @Author  : Jackey-lu
# @File    : 面试题59 - II. 队列的最大值.py

# class MaxQueue:
#
#     def __init__(self):
#         self.queue = []
#
#     def max_value(self) -> int:
#         if not self.queue:
#             return -1
#         return max(self.queue)
#
#     def push_back(self, value: int) -> None:
#         self.queue.insert(0,value)
#
#     def pop_front(self) -> int:
#         if not self.queue:
#             return -1
#         val = self.queue.pop(len(self.queue)-1)
#         return val

import queue
class MaxQueue:

    def __init__(self):
        self.deque = queue.deque()
        self.queue = queue.Queue()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans