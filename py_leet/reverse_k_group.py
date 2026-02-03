from typing import Optional
from . import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        # keep track of the end of the previous section
        last = dummy
        while last.next:
            leader = last
            count = 0
            while leader.next and count < k:  # check that we can move k spaces forward
                leader = leader.next
                count += 1

            if count < k:
                break

            first = leader.next  # nextGroup
            second = last.next  # start of group

            for _ in range(k):
                if second is None:
                    raise NameError("Second should not be none")
                third = second.next
                second.next = first
                first = second
                second = third

            # reconnect
            temp = last.next  # old group start, now tail
            last.next = first  # new head
            last = temp

        return dummy.next
