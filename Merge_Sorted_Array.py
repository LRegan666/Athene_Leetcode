class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = n-1, m-1
        k = m+n-1
        while i > -1:
            if nums2[i] > nums1[j]:
                nums1[k] = nums2[i]
                i -= 1
            else:
                if j > -1:
                    nums1[k] = nums1[j]
                    j -= 1
                else:
                    nums1[k] = nums2[i]
                    i -= 1
            k -= 1


if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m, n = 3, 3
    nums2 = [2, 5, 6]
    machine = Solution()
    machine.merge(nums1, m, nums2, n)
    print(nums1)
