class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            digit = []
            while x != 0:
                digit.append(x % 10)
                x = x // 10
            length = len(digit)
            for i in range(length // 2):
                if digit[i] != digit[length - 1 - i]:
                    return False
            return True