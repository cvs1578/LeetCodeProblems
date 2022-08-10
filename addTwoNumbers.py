#Problem 2: Given two linked list with digits stored in reverse order and each digit containing a single list
#Add the two numbers and return the sum as a linked list.
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        temp = head
        carry = 0
        while l1 and l2:
            temp.val = l1.val + l2.val + carry
            if temp.val>=10:
                temp.val -=10
                carry=1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
            if l1 or l2 or carry == 1:
                temp.next = ListNode()
                temp = temp.next
        while l1:
            temp.val = l1.val+carry
            if temp.val>=10:
                temp.val -=10
                carry=1
            else:
                carry = 0
            l1 = l1.next
            if l1 or carry == 1:
                temp.next = ListNode()
                temp = temp.next
        while l2:
            temp.val = l2.val+carry
            if temp.val>=10:
                temp.val -=10
                carry=1
            else:
                carry = 0
            l2 = l2.next
            if l2 or carry==1:
                temp.next = ListNode()
                temp = temp.next
        if carry == 1:
            temp.val = 1
        return head