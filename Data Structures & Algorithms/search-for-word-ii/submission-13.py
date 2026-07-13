class TrieNode():
    def __init__(self):
        self.children = {} #key: char value: TrieNode
        self.is_end = False
        
    def addWord(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char] #keep walking down the chain
        node.is_end = True #mark it at the end

class Solution:
    #Create a Trie

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        #We want to build a Trie with the words given
        
        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            #Either it's out of bound, or the letter is not present in the Trie, if so we exit the loop immedately
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] not in node.children or (r,c) in visit:
                return
            


            visit.add((r,c))
            #Build the word from the ground up
            char = board[r][c]
            word += char
            node = node.children[char] #keep walking along the trie

            if node.is_end: #it's only a word after
                res.add(word)
                
            
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r,c)) #backtrack, remove it before we return

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

 
        return list(res)

        
