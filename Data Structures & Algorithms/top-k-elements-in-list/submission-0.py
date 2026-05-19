import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #have a hash table for counts
        
        nums_to_count = defaultdict(int)
        for num in nums:
            nums_to_count[num]+=1


        #heapq.heapify_max(nums_to_count)

        #return the n largest values and compare them based on the values in nums_to_count
        return heapq.nlargest(k, nums_to_count, lambda k: nums_to_count[k])

        #have a heap 






