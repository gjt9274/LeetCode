class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        segments = [0] * 4

        def backtrack(segId, segStart):
            # 终止条件
            # 如果找到4段，且字符串遍历完毕，则终止
            if segId == 4:
                if segStart == len(s):
                   ipAddr = ".".join(str(seg) for seg in segments)
                   res.append(ipAddr)
                return

            # 提前终止
            if segStart == len(s):  # 如果已经遍历完字符串，但是没有4段，则提前终止
                return

            # 由于ip地址每一段都不能有前导0，如果当前数字为0，则该段ip只能为0
            if s[segStart] == '0':
                segments[segId] = 0
                backtrack(segId + 1, segStart + 1)

            # 选择遍历列表
            addr = 0
            for i in range(segStart, len(s)):
                addr = addr * 10 + int(s[i])
                if 0 < addr <= 255:
                    segments[segId] = addr
                    backtrack(segId + 1, i + 1)
                else:
                    break
        backtrack(0, 0)
        return res
