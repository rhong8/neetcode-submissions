class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cumulativeCost = [0] * (len(cost) + 1)

        cumulativeCost[0] = 0
        cumulativeCost[1] = 0

        for i in range(2, len(cumulativeCost)):
            cumulativeCost[i] = min(cumulativeCost[i-1] + cost[i-1], cumulativeCost[i-2] + cost[i-2])


        return cumulativeCost[-1]
        