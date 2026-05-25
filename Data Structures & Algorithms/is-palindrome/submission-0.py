class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        

        #breaks it down to an array, only keeps those who are alphanumeric, then converts it back
        #to a string using ''.join
        s = ''.join(c for c in s if c.isalnum())
        idx_front = 0
        idx_end = len(s) - 1
        while(idx_front < idx_end):
            if(s[idx_front].lower() != s[idx_end].lower()):
                return False
            idx_front += 1
            idx_end -=1

        return True