class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(op, cl, curr):
            if op == 0 and cl == 0:
                res.append(curr)
            elif cl != 0 and op == 0:
                curr = curr + (')' * cl)
                backtrack(0, 0, curr)
            elif op != 0 and cl != 0:
                if (op < cl):
                    _curr = curr + ')'
                    backtrack(op, cl - 1, _curr )
                _curr2  = curr + '('
                backtrack(op - 1, cl, _curr2)

        backtrack(n - 1, n, '(')

        return res

            

                
            

