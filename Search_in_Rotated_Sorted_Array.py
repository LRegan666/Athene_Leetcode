class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = int((start + end) / 2)
            if nums[start] > nums[end]:
                avg = int((nums[start] + nums[end]) / 2)
                if avg <= nums[mid]:
                    if nums[end] < target <= nums[mid]:
                        end = mid
                    else:
                        start = mid
                else:
                    if target <= nums[mid] or target > nums[end]:
                        end = mid
                    else:
                        start = mid
            else:
                mid = int((start + end) / 2)
                if target <= nums[mid]:
                    end = mid
                else:
                    start = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 4
    finder = Solution()
    index = finder.search(nums, target)
    print(index)
