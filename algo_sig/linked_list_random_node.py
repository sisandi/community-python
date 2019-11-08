import random


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """

        self.head = head

    def getRandom(self) -> int:
        """Returns a random node's value."""

        node = self.head.next
        random_element = self.head.val
        events = 1

        while node:
            if random.randint(1, events+1) == 1:
                random_element = node.val

            node = node.next
            events += 1

        return random_element
