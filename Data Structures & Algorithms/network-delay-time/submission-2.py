import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
             #implement Dijkstra

            #Dijkstra's recipe:

            #Initialize adjList and Closest nodes heap
            dist = [float("inf")] * n #distances
            dist[k - 1] = 0
            adjList = defaultdict(list)
            for source, target, weight in times:
                adjList[source].append((weight, target))

                if source == k:
                    dist[target - 1] = weight

            closest = [] #a heap
            seen = set()
            

            #push weight-target onto the heap
            for wt in adjList[k]:
                heapq.heappush(closest, wt)
            

            #the last pop is guranteed to be the longest
            while closest:
                weight, target = heapq.heappop(closest)
                if target in seen: #already seen
                    continue

                seen.add(target)
                #calculate distances you can reach from the processed node
                #if dist(u, v) + dist(v, w) < dist(u, w)
                #so you need the adjList
                for w2, u in adjList[target]:
                    if weight + w2 < dist[u - 1]:
                        #problem
                        dist[u - 1] = weight + w2
                    heapq.heappush(closest, (dist[u-1], u)) #push all reachable nodes from that point. 
                    #by gurantee, it is not infinity.
            

            #if there is an unreachable node, that has time infty.
            
            #print(dist)

            res = max(dist)
            if res == float("inf"):
                 return -1 
            else:
                 return res


            
            

