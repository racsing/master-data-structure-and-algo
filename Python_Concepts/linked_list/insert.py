class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFirst(self, data):
        # Create a new node.
        new_node = Node(data)
        # If the linked list is empty set the new node as the Head.
        if self.head == None:
            self.head =  new_node
            return
        
        # Connect the new_node to the linked list.
        new_node.next = self.head
        # Update the Head pointer to new_node
        self.head = new_node


    def insertAtPosition(self, data, position):
        if position == 0:
            self.insertAtFirst(data)
            return
        counter = 0
        cur = self.head
        
        # Iterate over the linked list to find the node before the insertion point (position - 1).
        while cur.next != None:
            if position - 1 == counter:
                new_node = Node(data)
                new_node.next = cur.next
                cur.next = new_node
                return
            
            cur = cur.next
            counter += 1
        
        # If the cur pointer becomes None before reaching the position, the position is out of range.
        return
        

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head =  new_node
            return

        cur = self.head
        while cur.next:
            print(cur.data)
            cur = cur.next
        cur.next = new_node


    def length(self):
        cur = self.head
        size = 0
        while cur:
            size += 1
            cur = cur.next
        return size


    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        


if __name__ == '__main__':        
    linked_list = LinkedList()
   
   # Assign data 
    linked_list.insertAtEnd(2)
    linked_list.insertAtEnd(4)    
    linked_list.insertAtEnd(6)    
    # linked_list.insertAtFirst(0)

    print(linked_list.length())
    linked_list.display()
    