# Напиши функцию is_balanced(text), проверяющую правильность расстановки скобок трёх видов: круглых, квадратных и фигурных. Проверь на строках "({[]})", "([)]" и "((".

def is_balanced(text):
    stack = []
    braces = {']': '[', '}': '{', ')':'('}

    for char in text:
        if char in '[{(':
            stack.append(char)
        if char in ']})':
            if len(stack) == 0 or stack.pop() != braces[char]:
                return False
    if len(stack) == 0:
        return True
    return False

test_str = "({[]})"
print(f'Строка на проверке ({test_str}): {is_balanced(test_str)}')
print(f'Строка на проверке ([)]: {is_balanced('([)]')}')
print(f'Строка на проверке ((: {is_balanced('([)]')}')