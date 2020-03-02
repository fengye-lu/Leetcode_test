# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 12:10
# @Author  : Jackey-lu
# @File    : 两数相加.py

# class Solution(object):
# 	def addTwoNumbers(self, l1, l2):
# 		# 定义一个进位标志
# 		a,b,p,carry = l1,l2,None,0
# 		while a or b:
# 			# a和b节点的值相加，如果有进位还要加上进位的值
# 			val = (a.val if a else 0)+(b.val if b else 0)+carry
# 			# 根据val判断是否有进位,不管有没有进位，val都应该小于10
# 			carry,val = val/10 if val>=10 else 0,val%10
# 			p,p.val = a if a else b,val
# 			# a和b指针都前进一位
# 			a,b = a.next if a else None,b.next if b else None
# 			# 根据a和b是否为空，p指针也前进一位
# 			p.next = a if a else b
# 		# 不要忘记最后的边界条件，如果循环结束carry>0说明有进位需要处理这个条件
# 		if carry:
# 			p.next = ListNode(carry)
# 		# 每次迭代实际上都是将val赋给a指针的，所以最后返回的是l1
# 		return l1




class Solution:
    def addTwoNumbers(self, l1, l2):
        i1 = 1
        sum1 = 0
        i2 = 1
        sum2 =0
        l3 = None
        while l1:
            sum1 = l1.val *i1 + sum1
            l1 = l1.next
            i1 *= 10
        while l2:
            sum2 = l2.val *i2 + sum2
            l2 = l2.next
            i2 *= 10
        add = sum1+sum2
        while add > 0:
            rel = add % 10
            l3.val = rel
            add = add / 10
        return l3
