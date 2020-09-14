class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num

        res = [0, 0]
        # 获取最后一个 1 的位置
        diff = (diff & (diff-1)) ^ diff #因为两个单出来的数至少有一个位置不同，异或后为1
        for num in nums:
            if diff & num == 0:  #按最后一个1 的位置将数分组，然后组内异或，就得到了两个组内单出来的那个数，即结果
                res[0] ^= num
            else:
                res[1] ^= num
        return res
