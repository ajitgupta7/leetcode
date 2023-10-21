class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        if len(words) != len(pattern):
            return False

        word_to_pattern = {}
        pattern_to_word = {}

        for p, word in zip(pattern, words):
            if p not in pattern_to_word and word not in word_to_pattern:
                pattern_to_word[p] = word
                word_to_pattern[word] = p

            elif pattern_to_word.get(p) != word or word_to_pattern[word] != p:
                return False
        return True