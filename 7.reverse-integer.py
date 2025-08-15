class Solution(object):
    def reverse(self, x):
        flag = x >= 0
        digit = []
        if flag:
            digit.append(x % 10)
            x //= 10
        else:
            digit.append(-(x % -10))
            x //= -10
        while x > 0:
            digit.append(x % 10)
            x //= 10
        ret = 0
        for num in digit:
            ret = ret * 10 + num
        if flag:
            if ret <= 2147483647:
                return ret
        else:
            ret *= -1
            if ret >= -2147483648:
                return ret
        return 0