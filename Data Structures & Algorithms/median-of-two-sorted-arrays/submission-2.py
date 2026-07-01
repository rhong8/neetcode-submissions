class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        total = len(nums1) + len(nums2)

        half = total // 2
        if len(B) < len(A):
            A, B = B,A

        l, r = 0, len(A) - 1 #A is the smaller array

        while True: #Finding the partition is absolutely guranteed
            i = (l + r) // 2
            j = half - i - 2 #the index of the partition in the other array.
            #think about it like this: i and j are indices.
            #i + 1 + j + 1 = half       i + j + 2 = half
            #half = j + i - 2

            Aleft = A[i] if i >= 0 else float("-infinity") #we want this to be negative infty because we take the max of these two,
            #if it's out of bound, then there's no possible way that it will be chosen. 
            #if it's out of bound that means the partition of the left side lies in the right array.
            Aright = A[i + 1] if i + 1 < len(A) else float("infinity") 
            #same goes to here, we want the minimum of the two right pointers
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if j + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:

                if total % 2 == 1:
                    
                    return min(Aright, Bright) #the right partition has 1 more element, in that case we ned to find the minimum of the two
                
                
                return (min(Aright, Bright) + max(Aleft, Bleft)) / 2 #Find the two middle vals of the partitions and add em together
            elif Aleft > Bright: #Too many elements in a
                r = i -1
            else: #too few elements in b
                l = i + 1
            