# Create a linkedList

class Node:
    def __init__(self,data):
        # A node instance consists of a data attribute and a link
        self.data = data
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None 
        
    def append(self,data):
        newNode = Node(data)    
        
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            
            while current.next:
                current = current.next
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
                
        
