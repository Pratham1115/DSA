class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

        return dummy.next