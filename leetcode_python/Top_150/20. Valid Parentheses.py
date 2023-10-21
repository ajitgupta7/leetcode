class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)):
            s = s.replace('()', "").replace('{}',"").replace('[]',"")
        return s==""