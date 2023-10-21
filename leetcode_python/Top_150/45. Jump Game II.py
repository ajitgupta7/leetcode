class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## simplified BFS

        jump = 0
        l = r = 0

        while r < len(nums)-1:
            reach = 0
            for i in range(l, r+1):
                reach = max(reach, i+nums[i])
            l = r+1
            r = reach
            jump += 1
        return jump