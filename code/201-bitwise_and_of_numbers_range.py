class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 先求最长公共前缀，右移直到相等
        # 然后后面全部为0，左移相同的位数
        cnt = 0
        while m != n:
            m = m >> 1
            n = n >> 1 
            cnt += 1
        return (m << cnt)
