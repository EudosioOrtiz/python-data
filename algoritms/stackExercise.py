from collections import deque

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
    
    def reverse_string(self, phrase):
        reversePhrase = ""
        for letter in phrase:
            self.push(letter)
        while self.container:
            reversePhrase += self.peek()
            self.pop()
        return reversePhrase

s = Stack()
print(s.reverse_string("We will conquere COVID-19"))
print(s.reverse_string("I am the king"))

def match_dic(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced( formula):
    stack = Stack()
    for ch in formula:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not match_dic(ch,stack.pop()):
                return False

    return stack.size()==0

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))