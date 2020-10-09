class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 1 or len(intervals[0]) < 1:
            return []
        res = []
        intervals = sorted(intervals)
        first = intervals[0][0]
        second = intervals[0][1]
        for i in range(1, len(intervals)):
            item = intervals[i]
            if item[0] <= second:
                if item[1] <= second:
                    continue
                else:
                    second = item[1]
            else:
                res.append([first, second])
                first = item[0]
                second = item[1]
        res.append([first, second])
        return res
