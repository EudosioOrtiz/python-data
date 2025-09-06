s = []
s.append('https://cnn.com/')
s.append('https://cnn.com/world')
s.append('https://cnn.com/india')
s.append('https://cnn.com/china')

s[-1]
s.pop()
s.pop()
s.pop()

#recomended

from collections import deque
stack =deque()
#read documentation of deque
stack.append('https://cnn.com/')
stack.append('https://cnn.com/world')
stack.append('https://cnn.com/india')
stack.append('https://cnn.com/china')
stack.pop()

#queue created
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)