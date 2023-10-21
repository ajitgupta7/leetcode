class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sub = True
        start = 0
        find = ""
        for i in s:
            for j in range(start,len(t)):
                if i == t[j]:
                    start = j+1
                    find += t[j]
                    break
        return find == s