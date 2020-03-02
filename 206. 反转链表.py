# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 20:02
# @Author  : Jackey-lu
# @File    : 206. 反转链表.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        rel_head = ListNode(None)
        mid_val = head
        sec_val = head
        a = []
        while mid_val:
            a.insert(0,mid_val.val)
            mid_val = mid_val.next
        for i in a:
            rel_head,rel_head.val =sec_val,i
            sec_val = sec_val.next
            rel_head.next = sec_val
        return head