class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return []
        L = len(numbers)
        end_index = L-1
        for i in range(L):
            if numbers[i] >= target:
                end_index = i
        start, end = 0, end_index
        while start < end:
            two_sum = numbers[start] + numbers[end]
            if two_sum == target:
                return [start+1, end+1]
            if two_sum < target:
                start += 1
            else:
                end -= 1
        return []


if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 9
    finder = Solution()
    res = finder.twoSum(numbers, target)
    print(res)
