from typing import List


class Solution:
    def deserialize(self, s: str) -> List:
        from queue import LifoQueue as Stack
        stack = Stack()
        current_list = None
        current_number = None
        for l in s:
            if l == '[':
                if current_list is not None:
                    stack.put(current_list)
                current_list = []
                current_number = 0
            elif l.isnumeric():
                current_number = current_number or 0 * 10 + int(l)    
            elif l == ",":
                current_list.append(current_number)
            elif l == ']':
                if current_number is not None:
                    current_list.append(current_number)
                if stack.empty():
                    return current_list
                parent_list = stack.get()
                parent_list.append(current_list)
                current_number = None
                current_list = parent_list
        return current_list


print(Solution().deserialize("[123,[456,[789]]]"))

