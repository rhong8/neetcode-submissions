class WordDictionary:
    
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False
        
    def __init__(self):
        self.root = self.TrieNode() #Dummy root

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children: #all of the next valid characters
                node.children[char] = self.TrieNode()
            node = node.children[char]
        node.is_end = True #ending the word

    def search(self, word: str) -> bool:
        self.exists = False
        print(f"Searching for {word}")
        def searchHelper(node, curr_word):
        
            '''
            if not curr_word:
                self.exists = True
                return
            '''
            if not curr_word:
                if node.is_end:
                    print("end")
                    self.exists = True
                
                return


            char = curr_word[0]
            print(f"Currently on {char}")

            if char == '.':
                for letter in node.children: #selecting next letter
                    print(f"Branching out to {letter}, {curr_word[1:]}")
                    searchHelper(node.children[letter], curr_word[1:]) #spawn in recursions
            elif char in node.children:
                print(f"Searching further: {curr_word[1:]}")
                searchHelper(node.children[char], curr_word[1:])
            else: #cannot be found
                return

            
        searchHelper(self.root, word)
        return self.exists

