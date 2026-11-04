class Solution:
    def checkValidString(self, s: str) -> bool:
        open_max = open_min = 0
        for c in s:
            if c == "(":
                open_max += 1
                open_min += 1
            elif c == ")":
                open_min -= 1
                open_max -=1
            else:
                open_min -= 1
                open_max += 1
            open_min = max(open_min, 0)
            if open_max < 0:
                return False
        return open_min == 0