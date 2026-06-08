class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        #recreating Neetcode's solution from scratch

        s1Count, s2Count = [0] *26, [0] * 26
        matches = 0
        #initialize character counts for s1, and the first iteration of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26): #loop through both arrays to count the matches
            if s1Count[i] == s2Count[i]:
                matches += 1


        l = 0
        print(f"{s1Count} {s2Count}")

        
        #start at the next index: s1
        for r in range(len(s1), len(s2), 1):
            print(f"matches: {matches}")
            if matches == 26: return True

            #freshly incremented r
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] + 1: #tipping the scales downwards
                matches -=1
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] - 1: #tipping the scales downwards
                matches -=1
            
            l += 1

        #check if matches is 26 at the final iteration
        return matches == 26
            