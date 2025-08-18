class Solution(object):
    def isMatch(self, s, p):
        l1, l2 = len(s), len(p)
        array = [[False] * (l1 + 1) for _ in range(l2 + 1)]
        index = 0
        array[0][0] = True
        while index < l2:
            if l2 > index + 1 and p[index + 1] == '*':
                for i in range(l1 + 1):
                    if array[index][i]:
                        array[index + 2][i] = True
                        for j in range(i, l1):
                            if p[index] == '.' or p[index] == s[j]:
                                array[index + 2][j + 1] = True
                            else:
                                break
                index += 2
            else:
                for i in range(l1):
                    if array[index][i]:
                        array[index + 1][i + 1] = p[index] == '.' or p[index] == s[i]
                index += 1
        return array[l2][l1]