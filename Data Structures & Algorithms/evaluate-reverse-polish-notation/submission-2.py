class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        mapping = {
            "+": lambda a , b : a + b,
            "-": lambda a , b : a - b,
            "*": lambda a , b : a * b,
            "/": lambda a , b : int(a / b)
        }
        for char in tokens:
            if char in mapping:
                val1 = stack.pop()
                val2 = stack.pop()
                operation = mapping[char](val2, val1)
                stack.append(operation)
            else:
                stack.append(int(char))
        return stack[0]
