class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if(len(s) %2 != 0):
            return False

        for char in s:
            if(char in ('(', '{', '[')):
                stack.append(char)
            else:
                if not stack:
                    return False #if the list is empty that means there's an imbalance
                temp = f"{stack.pop()}{char}"
                if temp not in ("()", "{}", "[]"):
                    return False
        
        if len(stack) != 0:
            return False

        return True

