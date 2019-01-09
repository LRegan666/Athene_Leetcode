class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        ln = len(nums)
        i, next_pos = 0, 0
        current_jump, last_jump = 0, i+nums[i]
        while i < ln:
            for j in range(i+1, last_jump+1):
                if j >= ln:
                    break
                tmp = j + nums[j]
                if tmp > current_jump:
                    current_jump = tmp
                    next_pos = j
            if current_jump >= ln-1:
                return True
            if current_jump == last_jump:
                return False
            last_jump = current_jump
            i = next_pos
        return False


if __name__ == '__main__':
    nums = [2, 0]
    judger = Solution()
    res = judger.canJump(nums)
    print(res)

