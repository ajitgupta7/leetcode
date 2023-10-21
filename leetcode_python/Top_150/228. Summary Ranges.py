class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []

        for num in nums:
            if ranges and ranges[-1][1] == num-1:
                ranges[-1][1] = num
            else:
                ranges.append([num, num])


        return ['->'.join(map(str, r)) if r[0] != r[1] else str(r[0]) for r in ranges]