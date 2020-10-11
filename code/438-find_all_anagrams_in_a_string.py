class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        need = defaultdict(lambda: 0)
        win = defaultdict(lambda: 0)

        for i in range(len(p)):
            need[p[i]] += 1

        begin = []
        left, right = 0, 0
        distance = 0

        while right < len(s):
            c = s[right]
            right += 1
            if need[c] != 0:
                win[c] += 1
                if win[c] == need[c]:
                    distance += 1
            while right-left >= len(p):
                if right-left == len(p) and distance == len(set(p)):
                    begin.append(left)
                d = s[left]
                left += 1
                if need[d] != 0:
                    if win[d] == need[d]:
                        distance -= 1
                    win[d] -= 1
        return begin
