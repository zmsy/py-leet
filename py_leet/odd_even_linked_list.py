from typing import Optional
from . import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode(-1, None)
        even_head = ListNode(-1, None)

        i = 1  # start at odd num
        cur = head
        odd_cur = odd_head
        even_cur = even_head
        while cur is not None:
            is_even = i % 2 == 0

            node = cur  # stash this node specifically
            cur = cur.next  # iterate cur
            node.next = None  # erase the link to the other list

            if is_even:
                even_cur.next = node
                even_cur = node
            else:
                odd_cur.next = node
                odd_cur = node

            i += 1

        odd_cur.next = even_head.next

        # return the odd list
        return odd_head.next
