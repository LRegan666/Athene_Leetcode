class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ld = len(digits)
        status = False
        for i in range(ld-1, -1, -1):
            digits[i] += 1
            if digits[i] >= 10:
                digits[i] %= 10
                status = True
            else:
                status = False
                break
        if status:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    digits = [0]
    computer = Solution()
    res = computer.plusOne(digits)
    print(res)

