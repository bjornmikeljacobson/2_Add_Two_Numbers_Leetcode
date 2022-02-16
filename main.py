# Definition for singly-linked list.

class LinkedList:
    def __init__(self):
        self.head = None


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


llist = LinkedList()
first_node = ListNode('a')
second_node = ListNode("b")
third_node = ListNode('c')
first_node.next = second_node
second_node.next = third_node
llist.head = first_node

print(first_node.val, first_node.next.val)

