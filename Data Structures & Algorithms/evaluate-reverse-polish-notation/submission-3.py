import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        stack = []
        operators = ['+', '-', '*', '/']
        for t in tokens:
            if t in ops:
                a = stack.pop() #pop the last one
                b = stack.pop() #pop the second to last
                print(f"{b} {t} {a}")
                result = int(ops[t](b,a)) #do the operation between a and b
                stack.append(result) #store result in stack
            else:
                stack.append(int(t))
                
        
        del ops
        
        return stack[0]