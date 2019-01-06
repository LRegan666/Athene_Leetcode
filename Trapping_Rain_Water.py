class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        L, res = len(height), 0
        left_max, right_max = [0]*L, [0]*L
        left_max[0], right_max[L-1] = height[0], height[-1]
        for i in range(1, L):
            left_max[i] = max(height[i], left_max[i-1])
        for j in range(L-2, -1, -1):
            right_max[j] = max(height[j], right_max[j+1])
        for k in range(L):
            res += min(left_max[k], right_max[k]) - height[k]
        return res


if __name__ == '__main__':
    height = [5,4,1,2]
    computer = Solution()
    res = computer.trap(height)
    print(res)
