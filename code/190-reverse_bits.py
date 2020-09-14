class Solution:
    def reverseBits(self, n: int) -> int:
        #可以类比十进制的反转
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1) #相当于十进制中 res * 10 + (n %10)
            n = n >> 1                 # n /= 10
        return res
