class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency_table = defaultdict(int)
        local_max_count:int = 0#the local maximum of a recurring character
        local_max_char = ''
        result = 0

        l = 0
        for r in range(len(s)):
            frequency_table[s[r]] += 1 #add a count
            if (frequency_table[s[r]] > local_max_count):
                local_max_count = frequency_table[s[r]]
                #local_max_char = s[r]
            while((r - l + 1) - local_max_count > k ): #while the window length - the local max is greater than k
                frequency_table[s[l]] -= 1
                l += 1 #slide l forwards
                local_max_count = max(local_max_count, frequency_table[s[l]])


        

            result = max(result, r - l +1)
        return result