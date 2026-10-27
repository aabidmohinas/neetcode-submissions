class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        p = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for ch in s:
            if ch not in p:
                stack.append(ch)
            else:
                try:
                    l = stack.pop()
                    if l != p[ch]:
                        return False

                except IndexError:
                    return False
        return not stack