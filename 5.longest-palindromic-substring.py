class Solution(object):
    def longestPalindrome(self, s):
        length = len(s)
        ret = s[0 : 1]
        middle = (length - 1) // 2
        for i in range(length):
            for j in range(middle + 1):
                if i - j >= 0 and i + j < length and s[i - j] == s[i + j]:
                    if len(ret) < j * 2 + 1:
                        ret = s[i - j : i + j + 1]
                else:
                    break
        for i in range(length - 1):
            if s[i] == s[i + 1]:
                for j in range(middle + 1):
                    if i - j >= 0 and i + 1 + j < length and s[i - j] == s[i + 1 + j]:
                        if len(ret) < j * 2 + 2:
                            ret = s[i - j: i + j + 2]
                    else:
                        break
        return ret