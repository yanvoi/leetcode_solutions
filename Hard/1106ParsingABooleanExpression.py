# O(n) time, O(n) space, stack solution
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operations = []
        bool_expressions = [[]]
        for char in expression:
            if char == "&" or char == "|" or char == "!": operations.append(char)
            elif char == "(": bool_expressions.append([])
            elif char == "t": bool_expressions[-1].append(True)
            elif char == "f": bool_expressions[-1].append(False)
            elif char == ")":
                operation = operations.pop()
                values = bool_expressions.pop()
                cur_result = None
                if operation == "&": cur_result = all(values)
                elif operation == "|": cur_result = any(values)
                else: cur_result = not values.pop()
                bool_expressions[-1].append(cur_result)

        return bool_expressions.pop().pop()
