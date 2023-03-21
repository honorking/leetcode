class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next
    
class Solution:
  //双指针
  def two_pointer_reverse(self, head):
    cur = ListNode(next=head)
    pre = ListNode()
    while cur.next != None:
      tmp = cur.next
      cur.next = pre
      
      pre = cur
      cur = temp
      
   return pre
  
  //递归
  def digui_reverse(self, head)：
    def reverse(pre,cur):
      if not cur:
        return pre
      
      temp = cur.next
      cur.next = pre
    
    return reverse(cur,temp)
  return reverse(None, head)
