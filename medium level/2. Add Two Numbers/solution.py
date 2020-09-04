# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result=ListNode()
        temp=result
        temp1,temp2=l1,l2
        carry=0
        while temp1 !=None or temp2!=None :
            x,y=0,0
            if temp1!=None:
                x=temp1.val
            if temp2!=None:
                y=temp2.val
            res_sum=carry+x+y
            carry = res_sum//10
            temp.next=ListNode(res_sum%10)
            temp=temp.next
            if temp1!=None:
                temp1=temp1.next
            if temp2!=None:
                temp2=temp2.next
        if carry >0:
            temp.next=ListNode(carry)
        return result.next
                
                