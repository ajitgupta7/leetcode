class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        trip, curr, start, n = 0, 0, 0, len(gas)

        for i in range(n):
            trip += gas[i] - cost[i]
            curr += gas[i] - cost[i]

            if curr < 0:
                start = i+1
                curr = 0
        return  start if trip>=0 else -1