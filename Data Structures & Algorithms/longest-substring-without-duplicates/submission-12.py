class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                #shrink the substring until it's valid
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            
            result = max(result, r - l + 1)

        return result
