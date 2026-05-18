class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # maps first occurence of an anagram to the list of all
        # the anagrams of that word
        # ex. if "cat" is seen first, the key would be ["cat","tac","act"]
        anagram_dict: dict[str, list[str]] = {}
        temp: str

        # this method returns true if the two strings are anagrams, false if not.
        def isAnagram(s: str, t: str) -> bool:
            #print(f"Anagram operation s: {s}")
            #print(f"Anagram operation t: {t}")
            char_count_s: dict[str, int] = {}
            char_count_t: dict[str, int] = {}

            # then they are anagrams
            for char in s:
                if char in char_count_s:
                    char_count_s[char] += 1
                else:
                    char_count_s[char] = 0

            for char in t:
                if char in char_count_t:
                    char_count_t[char] += 1
                else:
                    char_count_t[char] = 0

            #print(f"s keys: {char_count_s.keys()}")
            #print(f"t keys: {char_count_t.keys()}")
            #print(f"s values: {sorted(char_count_s.values())}")
            #print(f"t values: {sorted(char_count_t.values())}")

            if char_count_s.keys() != char_count_t.keys():
                return False

            for char in char_count_s.keys():
                if(char_count_s[char] != char_count_t[char]):
                    return False
                


            return True

        # returns the first occurence of that string's anagram if found,
        # returns None if not found
        def firstOccurence(s: str) -> str:
            nonlocal anagram_dict
            if(anagram_dict.keys() == None):
                return None

            for occ in anagram_dict:
                if isAnagram(occ, s):
                    return occ
            return None

        # loops through each string in strs, then compares it to the
        # first occurence of each anagram
        for s in strs:
            #print(f"Dealing with {s}")
            temp = firstOccurence(s)
            #print(f"temp: {temp}")
            # case where the anagram has occured before
            # simply append it to the end of the list that corresponds to the anagram
            if temp != None:
                anagram_dict[temp].append(s)
            else: #temp is none
                # anagram hasn't occured before, initalize a new list and append
                # that value
                anagram_dict.setdefault(s, []).append(s)
            #print()


        return list(anagram_dict.values())