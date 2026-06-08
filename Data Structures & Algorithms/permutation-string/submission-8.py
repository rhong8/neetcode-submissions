class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_arr = [0] * 26
        for c in s1:
            counts_arr[ord(c) - ord('a')] += 1 #make a counts array for s1
        

        temp_arr = [0] * 26
        l = 0
        r = len(s1) - 1
        for c in s2[l:r+1]: #initialize the FIRST  counts array
            temp_arr[ord(c) - ord('a')] += 1
        print(f"counts_arr: {counts_arr}")
        print(s2[l:r + 1])
        #print(f"first temp array result:  {temp_arr}")
        #print(f"r: {r}")

        while r < len(s2):
            print(f"loop iteration r is on {r}: ")
            print(f"temp array: {temp_arr}")
        
            if temp_arr == counts_arr:
                return True
            else:
                if r == len(s2)-1:
                    break
                print(s2[l:r+1])
                temp_arr[ord(s2[l]) - ord('a')] -=1 #erase letter at l, slide it forwards
                l += 1
                r += 1 #slide r forwards, add its corresponding letter to the count array
                
                temp_arr[ord(s2[r]) - ord('a')] +=1

        return False

