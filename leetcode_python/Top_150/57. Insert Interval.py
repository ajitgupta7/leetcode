class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
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