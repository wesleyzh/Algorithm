# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  # @return a ListNode
  def addTwoNumbers(self, l1, l2):
    carry = 0
    res = ListNode(0)
    head = res
    first = l1
    second = l2
    while first is not None or second is not None:
      if first is None:
        res.next = ListNode(second.val + carry)
        second = second.next
      elif second is None:
        res.next = ListNode(first.val + carry)
        first = first.next
      else:
        res.next = ListNode(first.val + second.val + carry)
        first = first.next
        second = second.next
      if res.next.val < 10:
        carry = 0
      else:
        res.next.val %= 10
        carry = 1
      
      res = res.next
      
    if carry != 0:
      res.next = ListNode(1)
      
    return head.next
    
    