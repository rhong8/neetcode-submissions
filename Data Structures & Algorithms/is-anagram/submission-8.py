class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         char_count_s: dict[str, int] = {}
         char_count_t: dict[str, int] = {}

         #then they are anagrams
         for char in s:
            if(char in char_count_s):
                char_count_s[char]+=1
            else:
                char_count_s[char] = 0
        
         for char in t:
            if(char in char_count_t):
                char_count_t[char]+=1
            else:
                char_count_t[char] = 0

         print(f"s keys: {char_count_s.keys()}")
         print(f"t keys: {char_count_t.keys()}")
         print(f"s values: : {sorted(char_count_s.values())}")
         print(f"t values: {sorted(char_count_t.values())}")

         if(char_count_s.keys() != char_count_t.keys()):
            return False
        

 
         

         if(sorted(char_count_s.values()) != sorted(char_count_t.values())):
            return False
        
         return True