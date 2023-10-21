class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        row_arr = [""] * numRows
        row_idx = 1
        down = True

        for letter in s:

            row_arr[row_idx - 1] += letter

            if row_idx == numRows:
                down = False
            elif row_idx == 1:
                down = True

            if down:
                row_idx += 1
            else:
                row_idx -= 1

        return "".join(row_arr)