class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        min_index = 0
        print("hi")
        while l <= r:
            mid = (l + r) //2

            if nums[mid - 1] > nums[mid]:
                min_index = mid
                break
            elif nums[mid] > nums[r]: #the rightmost value is a value less than the middle one, meaning somewhere, there is a pivot.
                l = mid + 1
            else:      
                #if the rightmost value is greater than the middle most value, the pivot is for sure in the bottom half.
                #there's no way for smaller values to be in the right half.
                r = mid - 1

        #now we have the minimum index. run two binary search on portion a and portion b.
        #print(min_index)
        def binarySearch(l, r, target):
            #print("Searching for ", target)
            while l <= r:
                #print("Running Search")
                mid = (l + r) // 2
                #print(f"Testing {nums[mid] == target}")
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target: 
                    l = mid + 1
                else: 
                    r = mid - 1
            return -1


        #print(f"Search 1: 0 to {min_index - 1} Serch 2: {min_index} to {len(nums) - 1}" )
        result = binarySearch(0, min_index-1, target)
        if result == -1:
            
            return binarySearch(min_index, len(nums) - 1, target)
        else:
            return result

        


        
