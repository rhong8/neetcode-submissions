class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        #push indicies as long as values are increasing
        for index, value in enumerate(temperatures):
            #print(index,value)
            #as long as temperatures are increasing:
            if not stack or value <= temperatures[stack[-1]]:
                stack.append(index)
            else:
                while stack and value > temperatures[stack[-1]]:
                    idx_to_assign = stack.pop()
                    print(idx_to_assign)
                    result[idx_to_assign] = index - idx_to_assign
                stack.append(index)

        
        print(stack)
        print(result)


        return result