class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stack = []
        L, max_area = len(heights), 0
        for i in range(L):
            if not stack:
                stack.append(i)
                continue
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                prev = stack[-1] if stack else -1
                w = i - prev - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        while stack:
            h = heights[stack.pop()]
            prev = stack[-1] if stack else -1
            w = L - prev - 1
            max_area = max(max_area, h * w)
        return max_area


if __name__ == '__main__':
    heights = [2,1,2]
    counter = Solution()
    res = counter.largestRectangleArea(heights)
    print(res)
