class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                res = 0
                if token == "+":
                    res = b + a
                elif token == "-":
                    res = b - a
                elif token == "*":
                    res = b * a
                elif token == "/":
                    res = int(b/a)  # 不能用板除
                stack.append(res)
        return stack[-1]
