from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def oneDifference(word1, word2):
            difference = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    difference += 1
                
                if difference > 1:
                    return False
            
            return difference == 1


        adjList = defaultdict(list)
        wordList.append(beginWord)

        for word1 in wordList:
            for word2 in wordList:
                if word1 != word2 and word1 not in adjList[word2] and oneDifference(word1,word2):
                    adjList[word1].append(word2)
                    adjList[word2].append(word1)
                

        print(adjList)
        count = 1
        q = deque()
        q.append(beginWord)
        seen = set()
        seen.add(beginWord)

        while q:
            #print(f"seen: {seen}")
            for w in range(len(q)):
                word = q.popleft()

            
                if word == endWord:
                    return count

            
                for cand in adjList[word]:
                    if cand in seen or cand in q:
                        continue
                    seen.add(cand)
                    q.append(cand)
            
            count += 1

        
        

        #bfs has to share a Q


        return 0

            