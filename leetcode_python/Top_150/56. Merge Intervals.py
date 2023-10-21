class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        I = []

        for curr in intervals:

            if I and curr[0] >= I[-1][0] and curr[0] <= I[-1][1] and curr[1] >= I[-1][1]:
                I[-1][1] = curr[1]

            elif I and curr[0] >= I[-1][0] and curr[0] <= I[-1][1] and curr[1] <= I[-1][1]:
                I[-1] = I[-1]

            else:
                I.append(curr)

        return I