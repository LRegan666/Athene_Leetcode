class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        if n < 2:
            for i in range(n+1):
                res.append(i)
            return res
        bins = ['00', '01', '11', '10']
        m = n - 2
        for _ in range(m):
            tmp = []
            for i in range(len(bins)):
                tmp.append('0'+bins[i])
            for j in range(len(bins)-1, -1, -1):
                tmp.append('1'+bins[j])
            bins = []
            bins.extend(tmp)
        for b in bins:
            res.append(int(b, 2))
        return res


if __name__ == '__main__':
    n = 2
    computer = Solution()
    res = computer.grayCode(n)
    print(res)

