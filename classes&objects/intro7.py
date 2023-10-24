# Create a linkedList

# Create the node of the linked->list
class Node:
    def __init__(self,data):
        # A node instance consists of a data attribute and a link
        self.data = data
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None #Initialise the start of the linkedList to None
        
    # Method to append a new node with data to the end of the linkedList, i.e: Creating links
    def append(self,data):
        newNode = Node(data)    # Create the node with the given data
        
        if self.head == None:
            # This executes if our linkedList is empty
            self.head = newNode
        else:
            # This block executes if our linkedList is not empty
            current = self.head
            
            while current.next: # This will execute until current.next != None
                current = current.next
            
            # Once we find the end, append the newNode to the end of the chain
            current.next = newNode
            
    # Method to display the linkedList
    def display(self):
        current = self.head         # Start from the head node
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
        return "\n"
    
if __name__ == "__main__":
    linked_List = linkedList()
    
# Append nodes
for i in range(5):
    linked_List.append(i)
    
print("Linked List: ", end=" ")
linked_List.display()
                
        
