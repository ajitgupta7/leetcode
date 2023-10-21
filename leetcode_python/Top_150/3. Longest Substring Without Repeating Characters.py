class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l, total = 0, 0
        res = set()

        for r in range(len(s)):

            while s[r] in res:
                res.remove(s[l])
                l += 1
            res.add(s[r])
            total = max(total, r - l + 1)

        return total
