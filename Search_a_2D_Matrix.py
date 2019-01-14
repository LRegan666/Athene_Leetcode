class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        start_row, end_row = 0, 0
        for i in range(m):
            end_row = i
            if target <= matrix[i][-1]:
                break
        for j in range(m):
            start_row = j
            if target <= matrix[j][0]:
                break
        if matrix[start_row][0] == target or matrix[end_row][-1] == target:
            return True
        if matrix[start_row][0] > target:
            start_row -= 1
        if matrix[end_row][-1] < target:
            return False
        return self.two_point_search(matrix[start_row], n, target)

    def two_point_search(self, nums, n, target):
        start, end = 0, n-1
        while start < end-1:
            mid = int((start + end) / 2)
            if target == nums[mid]:
                return True
            if target < nums[mid]:
                end = mid
            else:
                start = mid
        if target in (nums[start], nums[end]):
            return True
        return False


if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 30
    searcher = Solution()
    print(searcher.searchMatrix(matrix, target))

