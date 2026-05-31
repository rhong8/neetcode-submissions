class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
                idx_to_assign = stack.pop()
                result[idx_to_assign] = i - idx_to_assign
                print(i - idx_to_assign)
            
            stack.append(i)
        
    
        return result