class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            cur = s[i]
            if cur.isdigit():
                number = ""
                while s[i].isdigit():
                    number += s[i]
                    i += 1
                stack.append(number)
            elif cur.isalpha() or cur == '[':
                stack.append(cur)
                i += 1
            else:
                i += 1
                tmp = ""
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp  # 调整顺序，不需要反转
                stack.pop()
                repTime = int(stack.pop())
                push_str = ""
                while repTime:
                    repTime -= 1
                    push_str += tmp
                stack.append(push_str)
        return "".join(stack)
