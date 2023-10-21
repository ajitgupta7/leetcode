class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if not strs or len(strs) == 1:
            return [strs]

        dict_strs = {}
        for word in strs:
            key = ''.join(sorted(word))  # using a string as a key
            if key not in dict_strs:
                dict_strs[key] = [word]
            else:
                dict_strs[key].append(word)

        return list(dict_strs.values())