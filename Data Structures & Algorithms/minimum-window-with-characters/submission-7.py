class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def index(s: str) -> int:
            if s.islower():
                return ord(s) - ord('a')
            else:
                return ord(s) - ord('a') + 26

        if len(t) > len(s): 
            return ""
        charsT = [0] * 52
        windowChars = [0] * 52
        matches = 0
        unique = 0
        
        #this loop calculates the character occurences of the first t chars
        for i in range(len(t)):
            charsT[index(t[i])] += 1
            windowChars[index(s[i])] += 1
        
        for i in range(52):
            if charsT[i] != 0:
                unique += 1
            
            if windowChars[i] >= charsT[i] and charsT[i] != 0: #there can be a match even if there's more than a desired counting
                matches += 1
        #print(f"matches:  {matches} unique: {unique}")
        #The max number of matches is simply 26

        r = len(t)
        substring = s
        found_match = False
        
        print(r)

        if len(s) == len(t) and windowChars == charsT:
            return s

        for l in range(0, len(s) - len(t) + 1, 1):
            #print(f"l: {l}")
            while r < len(s) and matches < unique: #not enough matches
                #print(f"r: {r}")
                

                idx_r = index(s[r])
                

                windowChars[idx_r] += 1
                if windowChars[idx_r] == charsT[idx_r] and charsT[idx_r] != 0:
                    matches += 1
                    #print(f"incrementing matches by 1: {matches}")
                
                #recalculate matches
                r += 1
            if matches == unique:
                substring = min(substring, s[l:r], key = len)
                found_match = True
            
            idx_l = index(s[l])
            if charsT[idx_l] > 0 and windowChars[idx_l] - 1 < charsT[idx_l]:
                matches -= 1
            #print(f"Choosing between the two substrings: {substring} and {s[l:r+1]}")
            

            windowChars[idx_l] -= 1
        
        
        print(f"matches: {matches}")
        print(f" windowChars: {windowChars}")
        print(f" charsT: {charsT}")
        print(f" substring: {substring}")
        if not found_match:
            return ""

        return substring