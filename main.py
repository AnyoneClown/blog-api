def is_valid_parentheses(string: str):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    mismatch = []

    for index, char in enumerate(string):
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                mismatch.append(index)
            else:
                stack.pop()

    return not stack and not mismatch


def test_is_valid_parentheses():
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("[()]") == True
    assert is_valid_parentheses("{([])}") == True
    assert is_valid_parentheses("{[}]") == False
    assert is_valid_parentheses("(]") == False
    assert is_valid_parentheses("[(])((") == False
    assert is_valid_parentheses("(a)b[c]") == True
    assert is_valid_parentheses("(a)b[c}") == False
    assert is_valid_parentheses("(a)e}f") == False
    assert is_valid_parentheses("") == True


test_is_valid_parentheses()
