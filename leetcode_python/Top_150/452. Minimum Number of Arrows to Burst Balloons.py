class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points = sorted(points, key = lambda x:x[1])

        end = float("-inf")
        arrow = 0

        for baloon in points:
            if baloon[0] > end:
                arrow += 1
                end = baloon[1]

        return arrow