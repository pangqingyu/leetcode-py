class Solution(object):
    def myAtoi(self, s):
        ret = 0
        positive = True
        sign = True
        for c in s:
            if sign:
                if c == ' ':
                    continue
                elif c == '+':
                    sign = False
                elif c == '-':
                    positive = False
                    sign = False
                elif c >= '0' and c <= '9':
                    ret = int(c)
                    sign = False
                else:
                    break
            else:
                if '0' <= c <= '9':
                    ret = ret * 10 + int(c)
                else:
                    break
        if positive:
            if ret > 2147483647:
                return 2147483647
            else:
                return ret
        else:
            ret *= -1
            if ret < -2147483648:
                return -2147483648
            else:
                return ret