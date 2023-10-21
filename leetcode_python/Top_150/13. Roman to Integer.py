class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        s_split = [i for i in s]
        sum = 0
        for i in range(len(s_split)-1):
            if roman[s_split[i]] >= roman[s_split[i+1]]:
                sum += roman[s_split[i]]
            else:
                sum -= roman[s_split[i]]

        sum += roman[s_split[len(s_split)-1]]
        return sum