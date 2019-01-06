class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = ''
        for i in range(n):
            if i == 0:
                seq = '1'
            else:
                j, c = 0, 1
                tmp = ''
                while j < len(seq)-1:
                    if seq[j+1] == seq[j]:
                        c += 1
                    else:
                        tmp = tmp + str(c) + seq[j]
                        c = 1
                    j += 1
                tmp = tmp + str(c) + seq[j]
                seq = tmp
        return seq


if __name__ == '__main__':
    n = 1
    counter = Solution()
    res = counter.countAndSay(n)
    print(res)
