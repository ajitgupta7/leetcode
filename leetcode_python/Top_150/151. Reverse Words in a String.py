class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse = ""
        words = s.strip().split(" ")
        words = words[::-1]

        for i in range(len(words)):

            if words[i]:
                reverse += words[i]
                if i != len(words)-1:
                    reverse += " "

        return reverse