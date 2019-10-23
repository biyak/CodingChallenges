 #Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reversell(head: ListNode):
    prevNode = None
    node = head

    while(node != None):
        oldNext = node.next
        newNext = prevNode
        node.next = newNext
        prevNode = node
        node = oldNext

def printList(head:ListNode):
    node = head
    while(node != None):
        print(node.val)
        node = node.next

def reverseBetween(head: ListNode, m: int, n: int):
    prevNode = None
    node = head
    start = 1
    stop = 1

    while(stop <= n-1):
        
        if(node != None and start >= m):
            if(start == m):
                startNode = node
            oldNext = node.next
            newNext = prevNode
            node.next = newNext
            prevNode = node
            node = oldNext
            print(node.val)
        else: node = node.next ; start = start + 1; stop = stop + 1

    startNode.next = node
    
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8

reverseBetween(l1, 3, 7)
