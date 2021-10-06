class Node:  
    def __init__(self, data=None):  
        self.data = data  
        self.next = None  
       
      
      
class Stack:  
    def __init__(self):  
        self.top = None  
        self.size = 0  
        
    def push(self, data):  
    # create a new node 
        node = Node(data)  
        if self.top:  
            node.next = self.top  
            self.top = node                  
        else:  
            self.top = node  
            self.size += 1       
        
        
        
        
words = Stack()
words.push('4')
words.push('5')
words.push('6')
words.push('7')

#print the stack elements.
current = words.top
while current:
    print(current.data)
    current = current.next





