class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, total = 0, 0
        result = float("inf")

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                total = total - nums[l]
                result = min(result, r - l + 1)
                l += 1

        return result if result != float("inf") else 0