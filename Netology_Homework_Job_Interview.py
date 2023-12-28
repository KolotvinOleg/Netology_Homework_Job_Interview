# Task 1
class Stack:

    def __init__(self, data=None):
        if data:
            self.data = list(data)
        else:
            self.data = []

    def is_empty(self):
        return not self.data

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def size(self):
        return len()


# Task 2
def check_balance(string: str) -> str:
    my_stack = Stack(string)
    count_1 = 0
    count_2 = 0
    count_3 = 0
    prev_element = 0
    while my_stack.data:
        element = my_stack.pop()
        if element == '(':
            count_1 += 1
        elif element == '[':
            count_2 += 1
        elif element == '{':
            count_3 += 1
        elif element == ')':
            count_1 -= 1
        elif element == ']':
            count_2 -= 1
        else:
            count_3 -= 1
        if count_3 < 0 or count_2 < 0 or count_1 < 0:
            return 'Несбалансированно'
        if prev_element:
            # Проверка на такие случаи как {{[(])}}
            if element == ']' and prev_element in ['(', '{']:
                return 'Несбалансированно'
            if element == '}' and prev_element in ['[', '(']:
                return 'Несбалансированно'
            if element == ')' and prev_element in ['[', '{']:
                return 'Несбалансированно'
        prev_element = element
    if count_1 == 0 and count_2 == 0 and count_3 == 0:
        return 'Сбалансированно'


if __name__ == '__main__':
    print(check_balance('[[{())}]'))
