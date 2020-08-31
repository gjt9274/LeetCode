class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i,num in enumerate(nums):
            another_num = target - num
            if another_num in table:
                return (table[another_num],i)
            table[num] = i
        return (0,)