class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window  = {}, {} #dictionary to track the counts
        
        for c in t:
            countT[c] = countT.get(c,0) + 1 #getOrDefault
        

        need = len(countT) #num of unique chars


        have = 0
        res, resLen = [-1,-1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                #update our result first
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l,r]
                #pop s[l] from window[c]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l +=1


        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
                 
            
        