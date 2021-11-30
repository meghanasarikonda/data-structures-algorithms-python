from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, elem):
        self.container.append(elem)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(str):
    stack = Stack()
    reverse_str = ''
    for char in str:
        stack.push(char)

    while stack.size():
        reverse_str += stack.pop()

    return reverse_str


def is_match(ch1, ch2):
    match_dict = {'}': '{', ']': '[', ')': '('}
    return match_dict[ch1] == ch2


def is_balanced(str):

    parens = ['}', ')', ']', '(', '[', '{']
    stack = Stack()
    for char in str:
        if char in parens:
            if char in [')', ']', '}']:
                if stack.is_empty() or not is_match(char, stack.pop()):
                    return False
            if char in ['(', '[', '{']:
                stack.push(char)
    return stack.is_empty()


print(reverse_string("We will conquere COVID-19"))
print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
