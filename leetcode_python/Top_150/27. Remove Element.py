class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = [x for x in nums if x!=val]
        # for some reason nums[:] works in leetcode and not nums
        if nums != []:
            return len(nums)
        else:
            return 0