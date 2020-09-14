
# 方法1： 直接计算每个数的二进制数 1 的数目
class Solution:
    def countBits(self, num: int) -> List[int]:

        def count(n):
            cnt = 0
            while n != 0:
                n = n & (n-1)
                cnt += 1
            return cnt

        res = [0] * (num+1)
        for i in range(num+1):
            res[i] = count(i)
        return res

#方法2： 动态规划


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]*(num+1)
        for i in range(num+1):
            if (i & 1) == 0:
                res[i] = res[i//2]  # 二进制中乘以2，相当于左移1位，1的个数不变
            else:
                res[i] = res[i-1] + 1  # 等于其前一个数+1
        return res
