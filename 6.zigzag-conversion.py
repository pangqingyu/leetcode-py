class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        half_stride = numRows - 1
        stride = 2 * half_stride
        ret = s[0::stride]
        for j in range(1, half_stride):
            ret += ''.join(s[i] for i in range(len(s)) if i % stride in (j, stride - j))
        return ret + s[half_stride::stride]