class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        start, end = 0, len(nums)-1
        while start < end-1:
            mid = int((start + end) / 2)
            if nums[mid] == target:
                return True
            if nums[start] >= nums[end]:
                avg = int((nums[start] + nums[end]) / 2)
                if nums[mid] > avg:
                    if nums[start] <= target < nums[mid]:
                        end = mid
                    else:
                        start = mid
                elif nums[mid] == avg:
                    for j in range(start, end+1):
                        if nums[j] == target:
                            return True
                    return False
                else:
                    if target < nums[mid] or target >= nums[start]:
                        end = mid
                    else:
                        start = mid
            else:
                if nums[mid] > target:
                    end = mid
                else:
                    start = mid
        if nums[start] == target or nums[end] == target:
            return True
        return False


if __name__ == '__main__':
    nums = [3,5,1]
    target = 1
    finder = Solution()
    print(finder.search(nums, target))
