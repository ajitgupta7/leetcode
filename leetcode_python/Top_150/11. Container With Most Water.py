class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        area = 0
        idx1, idx2 = 0, len(height)-1

        while idx1 < idx2:

            v = (idx2 - idx1) * min(height[idx1], height[idx2])
            area = max(area, v)

            if height[idx1] <= height[idx2]:
                idx1 += 1
            else:
                idx2 -= 1

        return area