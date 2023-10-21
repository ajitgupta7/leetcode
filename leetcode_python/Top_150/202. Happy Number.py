class Solution(object):

    def get_square_values(self, N):
        number = [int(i) for i in str(N)]
        l = len(number)

        sum = 0
        for i in number:
            sum += i ** 2
        return sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_square_values(n)

        if n == 1:
            return True
        else:
            return False