class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        start = 0
        end = 0
        res = 0
        while end < len(s):
            if s[end] in char_set:
                while s[start] != s[end]:
                    char_set.remove(s[start])
                    start += 1
                start += 1
                end += 1
            else:
                char_set.add(s[end])
                end += 1
                if end - start > res:
                    res = end - start
        return res