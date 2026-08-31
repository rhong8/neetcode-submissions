import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) == k: #at capacity, do heappushpop
                heapq.heappushpop(heap, num)
            else: #push the element on
                heapq.heappush(heap, num)

        return heap[0]
