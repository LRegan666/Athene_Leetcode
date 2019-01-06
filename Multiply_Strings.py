class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        l1, l2 = len(num1), len(num2)
        store_list = [0]*(l1+l2)
        pos = l1 + l2 - 1
        if l1 > l2:
            for i in range(l2-1, -1, -1):
                current_pos = pos
                for j in range(l1-1, -1, -1):
                    store_list[current_pos] += (ord(num1[j])-48)*(ord(num2[i])-48)
                    store_list[current_pos-1] += store_list[current_pos] // 10
                    store_list[current_pos] %= 10
                    current_pos -= 1
                pos -= 1
        else:
            for i in range(l1-1, -1, -1):
                current_pos = pos
                for j in range(l2-1, -1, -1):
                    store_list[current_pos] += (ord(num2[j])-48) * (ord(num1[i])-48)
                    store_list[current_pos-1] += store_list[current_pos] // 10
                    store_list[current_pos] %= 10
                    current_pos -= 1
                pos -= 1
        start = 0
        while store_list[start] == 0:
            start += 1
        return ''.join([str(num) for num in store_list[start:]])


if __name__ == '__main__':
    num1 = "2"
    num2 = "3"
    counter = Solution()
    res = counter.multiply(num1, num2)
    print(res)
