class PrefixTree:


    class TrieNode():

        def __init__(self):
            self.children = {}
            self.is_end = False #marks the end of a valid word

    def __init__(self):
        self.root = self.TrieNode() #Dummy root


    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            
            node = node.children[char]
        
        node.is_end = True

    def search(self, word: str) -> bool: 
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char] #walk down the chain
        
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        
        node = self.root

        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        

        return True