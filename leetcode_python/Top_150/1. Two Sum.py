class Solution:
    def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            store = {}
            for i in range(len(nums)):
                if target-nums[i] in store:
                    return [store[target-nums[i]], i]
                store[nums[i]] = i

            return []