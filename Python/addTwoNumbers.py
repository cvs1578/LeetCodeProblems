#Problem 2: Given two linked list with digits stored in reverse order and each digit containing a single list
#Add the two numbers and return the sum as a linked list.
#Definition for singly-linked list.
class ListNode(object): #This is the Linked list def in LeetCode
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
        head = ListNode() #Answer will be a linked list, so first create a list
        temp = head #temp is going through the list
        carry = 0 #Carry because if the number is greater than 9 then we have to add 1
        while l1 and l2: #Go through each list
            temp.val = l1.val + l2.val + carry #Value will be first list + second + carry
            if temp.val>=10: #Determine if we have the carry
                temp.val -=10
                carry=1
            else:
                carry = 0
            #Next we will go through add to the linked list
            l1 = l1.next 
            l2 = l2.next
            #This will determine if the answer link list is appended
            if l1 or l2 or carry == 1:
                temp.next = ListNode()
                temp = temp.next
        while l1: #Only L1 has values
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
        while l2: #Only L2 has values
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
        if carry == 1: #See if there is a carry, then we just plop a 1 at the end
            temp.val = 1
        return head #Since we didn't move the head of the answer, we just return the head.