class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = [1] * len(nums)
        left = 1

        for i in range(1, len(nums)):
            left *= nums[i - 1]
            product[i] = left

        right = 1
        for j in range(len(nums) - 2, -1, -1):
            right *= nums[j + 1]
            product[j] *= right

        return product