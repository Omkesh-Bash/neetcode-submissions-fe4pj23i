class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for c in tokens:
            
            match c:
                case "+":
                    s.append(s.pop() + s.pop())
                case "-":
                    a, b = s.pop(), s.pop()
                    s.append(b - a)
                case "*":
                    s.append(s.pop() * s.pop())
                case "/":
                    a, b = s.pop(), s.pop()
                    s.append(int(b / a))
                case _:
                    s.append(int(c))
        return s[0]