class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        charSet = set()
        maxCount = 0
        maxString = ""
        temp = 0
        while(r < len(s)):
            if s[r] in charSet:
                print(f"match found. conflicting char: {s[r]} set: {charSet}")
                print(f"throwing away {s[l]}")
    
                while s[r] in charSet:
                    
                    charSet.discard(s[l])
                    l +=1
                maxCount = max(maxCount, temp)
                maxString  = s[r-maxCount:r]
                

                
                #charSet.discard(s[l])
                print(f"current window: {temp}")
            
               
            temp = r - l + 1#the difference between the indexes + 1 is the length
            charSet.add(s[r])
            r +=1
                
        maxCount = max(maxCount,temp) # "cash out" counts in temp, 
        #it applies if the last substring is the longest one
        print(maxString)
        del charSet
        return maxCount