import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist_map = {}
        h = []


        for coord in points:
            x = coord[0]
            y = coord[1]


            distance = math.sqrt((x**2) + (y**2))
            print(f"The distance from {(x,y)} to the origin is {distance}")
            dist_map[(x,y)] = distance

        print(dist_map.items())
        for coord, distance in dist_map.items():
            x, y = coord

            heapq.heappush(h,(-1 * distance, (x,y))) #maxheap
            if len(h) > k:
                print(f"Removing {h[0]} now..") #this is the largest element
                heapq.heappop(h)
        
        print("heap: ", h)


        for i in range(k):
            h[i] = list(h[i][1])
        

        return h