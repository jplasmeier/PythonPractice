# Practice With Stacks and Queues
# Python 2.7
# J. Plasmeier | jplasmeier@gmail.com
# MIT License
import random,copy

class Stack:
    def __init__(self):
        self.items = []

    def push(self, elt):
        self.items.append(elt)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items != []:
            return self.items[-1]
        else:
            return 

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

def check_parens(string):
    #Given a string, return true if the parens are balanced.
    stack = Stack()
    for c in string:
        if c == ')' and stack.peek() == '(':
            stack.pop()
        elif c =='(':
            stack.push(c)
        elif c == ')':
            stack.push(c)
    return stack.isEmpty()

def test_stack():
	s = Stack()
	print s.isEmpty
	s.push(3)
	s.push(5)
	s.push(7)
	print s.size()
	print s.pop()
	print s.pop()

expr = "()(wrong))()"
#expr = ")(false)("
#expr = "((hello)what is good(with) it)(man)() dude"
print check_parens(expr)
