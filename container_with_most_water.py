class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end = 0, len(height)-1
        max_aera = 0
        while start < end:
            tmp_aera = (end - start) * min(height[start], height[end])
            max_aera = max(max_aera, tmp_aera)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_aera


if __name__ == '__main__':
    h = [1,8,6,2,5,4,8,3,7]
    counter = Solution()
    res = counter.maxArea(h)
    print(res)