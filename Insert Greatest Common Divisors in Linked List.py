class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next
        while cur:
            gcd = math.gcd(cur.val, prev.val)
            g = ListNode(gcd)
            prev.next = g
            g.next = cur
            prev = cur
            cur = cur.next
        return head
# Given the head of a linked list head, in which each node contains an integer value
# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
