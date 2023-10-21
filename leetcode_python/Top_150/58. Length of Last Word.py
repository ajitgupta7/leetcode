class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = split(strip(s), " ")
        return len([i for i in string[-1]])