class Solution:
    def largestRectangleArea(self, heights) -> int:
        if len(heights) == 0:
            return 0
        st = []
        st.append(0)
        ans = 0
        for i in range(len(heights)):
            while len(st) != 0 and heights[st[-1]] > heights[i]:
                cur = st.pop()
                h = heights[cur]
                if len(st) == 0:
                    ans = max(ans, i * h)
                else:
                    ans = max(ans, (i - st[-1] - 1) * h)
            st.append(i)
        return ans

if __name__ == "__main__":
    h = [2, 1, 5, 6, 2, 3]
    s = Solution()
    ans = s.largestRectangleArea(h)
    print(ans)
    
