class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" or None:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []

        def backtrack(string, i):
            if len(string) == len(digits):
                result.append(string)
                return
            
            #for each character in the pone dictionary
            for char in phone[digits[i]]:
                new_string = string + char
                backtrack(new_string, i + 1) #keep searching along


        backtrack("", 0)
        return result