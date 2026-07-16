class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def backtrack(string, open_count, close_count):
            #base case:
            if len(string) == 2 * n:
                res.append(string)
                return

            if open_count < n:
                backtrack(string + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(string + ')', open_count, close_count + 1)

        backtrack('', 0, 0)   
        return res