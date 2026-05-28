class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) %2 != 0):
            return False
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in closeToOpen: #encountering ) ] }
                if stack and stack[-1] == closeToOpen[char]: #if the stack is nonempty, and the two chars pair
                    stack.pop() #pop the corresponding front end
                else:
                    return False
            else:
                stack.append(char) #append other chars to the stack


        #True if stack is empty, else False
        return True if not stack else False