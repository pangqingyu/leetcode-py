class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        extra = 0
        ret = ListNode(0)
        head = ret
        while l1 is not None or l2 is not None:
            if l1 is None:
                head.next = ListNode(l2.val)
                l2 = l2.next
                head = head.next
            elif l2 is None:
                head.next = ListNode(l1.val)
                l1 = l1.next
                head = head.next
            else:
                head.next = ListNode(l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next
                head = head.next
            if extra > 0:
                head.val += 1
                extra = 0
            if head.val >= 10:
                head.val -= 10
                extra = 1
        if extra > 0:
            head.next = ListNode(1)
        return ret.next