from queue import LifoQueue as Stack
from typing import Any


brackets_map = {
    ")":"(", "]":"[", "}":"{"
}
def check_valid_brackets(bracket_sequence: str) -> bool:
    stack = Stack()
    for b in bracket_sequence:
        if b in brackets_map.values():
            stack.put(b)
        else:
            if stack.empty() or stack.get() != brackets_map[b]:
                return False
    return True
            
            


if __name__ == "__main__":
    valid_brackets = "(())[({})]{}"
    res = check_valid_brackets(valid_brackets)
    assert res == True
    invalid_brackets = "(())[({})]{}]]"
    res = check_valid_brackets(invalid_brackets)
    assert res == False