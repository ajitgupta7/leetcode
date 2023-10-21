class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = {}

        for i in range(len(numbers)):

            if target - numbers[i] in store:
                return [store[target - numbers[i]]+1, i+1]
            store[numbers[i]] = i
        return []