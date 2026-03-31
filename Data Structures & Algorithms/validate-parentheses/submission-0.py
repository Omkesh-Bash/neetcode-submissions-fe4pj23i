class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h = {')' : '(', ']' : '[', '}' : '{'}
        for c in s:
            if c in h:
                if stack and h[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            # print(stack)
        return True if not stack else False