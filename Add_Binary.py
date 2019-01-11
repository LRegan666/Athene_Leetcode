class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la, lb = len(a), len(b)
        a, b = list(a), list(b)
        carry = False
        if la > lb:
            l_max, l_min = la, lb
            s_max, s_min = a, b
        else:
            l_max, l_min = lb, la
            s_max, s_min = b, a
        j = -1
        for i in range(l_max-1, -1, -1):
            if abs(j) > l_min and not carry:
                break
            if carry:
                if s_max[i] == '1':
                    s_max[i] = '0'
                else:
                    s_max[i] = '1'
                    carry = False
            if abs(j) <= l_min:
                if s_max[i] == '0':
                    s_max[i] = s_min[j]
                else:
                    if s_min[j] == '1':
                        s_max[i] = '0'
                        carry = True
                j -= 1
        if carry:
            s_max.insert(0, '1')
        return ''.join(s_max)


if __name__ == '__main__':
    a, b = "1010", "1011"
    counter = Solution()
    res = counter.addBinary(a, b)
    print(res)

