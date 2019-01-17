class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        return max(count_dict, key=count_dict.get)


if __name__ == '__main__':
    nums = [3,2,3]
    finder = Solution()
    res = finder.majorityElement(nums)
    print(res)

