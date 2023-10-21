class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if len(stack) < 2:
                    # Not enough numbers to perform the operation
                    return "Error: Malformed RPN expression"

                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # To ensure integer division result like in Python 2
                    stack.append(int(float(a) / b))

        if len(stack) != 1:
            return "Error: Malformed RPN expression"

        return stack[0]