import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #have a hash table for counts
        nums_counts = defaultdict(int)
        frequency_table = [[] for i in range(len(nums)+1)]
        res = []

        for n in nums:
            nums_counts[n]+=1
        
        for num,count in nums_counts.items():
            frequency_table[count].append(num)

        values_added = 0
        
        #going from the length of the nums to 0, decrementing by 1
        for i in range(len(nums), 0, -1):
            #checking each list in the frequency table
            for val in frequency_table[i]:
                #appending it until the total is k
               res.append(val)
               values_added +=1
               if(values_added == k):
                return res






