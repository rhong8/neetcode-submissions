#for loop strategy..

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
    
        def isPalindrome(s):
            j = 0
            k = len(s) - 1
            
            while j < k:
                if s[j] != s[k]:
                    return False
                j += 1
                k -= 1
                 
            return True

        def backtrack(path, start): 
              
            if start == len(s): #reached the end
                res.append(path[:])
                return

            #essentially continue. how can we continue here?
            
            

            for end in range(start + 1, len(s) + 1): #
                if not isPalindrome(s[start:end]):
                    continue
                path.append(s[start:end])
                backtrack(path, end)
                path.pop()


        print(isPalindrome(""))

        backtrack([], 0)


        return res