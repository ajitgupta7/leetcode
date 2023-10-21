class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        citations.sort(reverse = True)

        for i, elem in enumerate(citations):
            if elem >= i+1:
                h = i+1
        return h