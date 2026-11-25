
#no array dp
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        temp = 0 #initialize
        for i in range(2, n+1):
            temp = a + b
            a = b
            b = temp

        return b