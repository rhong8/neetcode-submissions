class Solution:


    def partition(self, s: str) -> List[List[str]]:


        def isPalindrome(s, i, j):
            a = i
            b = j

            while a <= b:
                if s[a] != s[b]:
                    return False
                    
                a += 1
                b -= 1

            return True


        res = []
        part = [] #only one possible partition

      
        def dfs(i):
            if i >= len(s):
                res.append(part[:]) #append a copy of the partition
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1) #you search the index after
                    part.pop()

        dfs(0)
        return res
            
