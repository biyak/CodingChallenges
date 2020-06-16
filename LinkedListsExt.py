#A clean implementation of a linked list

class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def get_value(self):
        return self.val

    def get_next(self):
        return self.next

    

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, node):
        #While head doesn't have a next
        if not self.head:
            self.head = node
        else:
            next = self.head
            while next:
                prev = next
                next = next.next
            prev.next = node
            
    def delete(self, val):
        node = self.head
        prev = None
        while node:
            if node.val == val:
                #You need to point the one before to the one after
                if prev == None:
                    #the head needs to be removed
                    self.head = self.head.next
                else: prev.next = node.next
            prev = node
            node = node.next

    def print(self):
        node = self.head
        l = ""
        while node:
            l = l + str(node.val) + " -> " 
            node = node.next
        l = l + "Null"
        print(l)

        
class SortedLinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, node):
        #If it's an empty linkedlist then start one
        if not self.head:
            self.head = node
        else:
            next = self.head
            prev = None
            while next:
                if next.val <= node.val:
                    if prev == None:
                        #next is the head and now must be moved over
                        self.head = node
                        node.next = next
                        return
                    else:
                        prev.next = node
                        node.next = next
                        return
                else:  prev = next; next = next.next #yeesh
            prev.next = node
            
    def delete(self, val):
        node = self.head
        prev = None
        while node:
            if node.val == val:
                #You need to point the one before to the one after
                if prev == None:
                    #the head needs to be removed
                    self.head = self.head.next
                else: prev.next = node.next
            prev = node
            node = node.next

    def delete_node(self, dnode):
        node = self.head
        prev = None
        while node:
            if node == dnode:
                #You need to point the one before to the one after
                if prev == None:
                    #the head needs to be removed
                    self.head = self.head.next
                else: prev.next = node.next
            prev = node
            node = node.next
            
    def print(self):
        node = self.head
        l = ""
        while node:
            l = l + str(node.val) + " -> " 
            node = node.next
        l = l + "Null"
        print(l)

class CircularLinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, node):
        #While head doesn't have a next
        if not self.head:
            self.head = node
        else:
            next = self.head
            while next.next != self.head:
                prev = next
                next = next.next
            prev.next = node
            
    def delete(self, val):
        node = self.head
        prev = None
        while node:
            if node.val == val:
                #You need to point the one before to the one after
                if prev == None:
                    #the head needs to be removed
                    self.head = self.head.next
                else: prev.next = node.next
            prev = node
            node = node.next

    def delete_node(self, dnode):
        node = self.head
        prev = None
        while node:
            if node == dnode:
                #You need to point the one before to the one after
                if prev == None:
                    #the head needs to be removed
                    self.head = self.head.next
                else: prev.next = node.next
            prev = node
            node = node.next
            
    def print(self):
        node = self.head
        l = ""
        while node:
            l = l + str(node.val) + " -> " 
            node = node.next
        l = l + "Null"
        print(l)
        
        
n1 = Node(10)
n2 = Node(11)
n3 = Node(5)
n4 = Node(10)
n5 = Node(0)
n6 = Node(-1)
##
##LL = LinkedList(n1)
##
##LL.insert(n2)
##
##LL.insert(n3)
##
##LL.print()

##LL.delete(5)
##
##LL.print()
##
##LL.delete(10)
##LL.print()


L2 = SortedLinkedList(n1)
L2.insert(n2)
L2.insert(n3)
L2.print()
L2.insert(n4)
L2.insert(n5)
L2.insert(n6)


L2.print()

L2.delete_node(n2)

L2.print()



