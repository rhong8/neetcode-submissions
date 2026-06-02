class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #solution: count the character numbers in each string
        #put them in a dictionary. array with 26 spots
        dict = defaultdict(list) #List[int] -> List[string]

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c.lower()) - ord('a')] +=1 #assign count to that letter
            dict[tuple(arr)].append(s)
        

        return list(dict.values())



            #check if it's already present in the dictionary

