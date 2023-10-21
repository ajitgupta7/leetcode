class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []

        res = set()

        n, p, z = [], [], []

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        N, P = set(n), set(p)

        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

            if len(z)>=3:
                res.add((0, 0, 0))
                print(res)

        from itertools import combinations

        for x, y in combinations(n, 2):
            target = -1*(x+y)
            if target in P:
                res.add(tuple(sorted([x, y, target])))

        for x, y in combinations(p, 2):
            target = -1*(x+y)
            if target in N:
                res.add(tuple(sorted([x, y, target])))


        return [list(x) for x in res]