class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        mj = 0
        for i, elem in enumerate(nums):
            if i > mj:
                return False
            mj = max(mj, i+elem)
        return True