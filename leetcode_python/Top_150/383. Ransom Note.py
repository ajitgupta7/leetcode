class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        word_dict = {}

        for letter in magazine:
            if letter not in word_dict:
                word_dict[letter] = 1
            else:
                word_dict[letter] += 1

        for letter in ransomNote:
            if letter in word_dict and word_dict[letter] > 0:
                word_dict[letter] -= 1
            else:
                return False
        return True