class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sentence = ''.join(lower(c) for c in s if c.isalnum() and c!=" ")
        return sentence == sentence[::-1]