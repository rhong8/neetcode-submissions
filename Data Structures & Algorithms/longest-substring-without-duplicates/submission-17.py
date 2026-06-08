class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        result = 0
        l = 0
        #abca
        r = 0
        for r in range(len(s)):
            while s[r] in charSet: #if we encounter a duplicate, then we need to advance l and remove until its gone
                charSet.remove(s[l])
                l += 1
                 #the length of the substring is r-l+1, so we need to take the max of that. as the string's getting longer,
                #it has the potential to update the result.
            charSet.add(s[r]) #add this new character to the set
            result = max(result, r - l +1)


        return result