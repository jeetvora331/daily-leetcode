class TrieNode:
    def __init__ (self):
        self.child = {}
        self.end = False
        

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root 
        
        for i in word:
            if i not in curr.child:
                curr.child[i] = TrieNode()
            curr = curr.child[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        for i in word:
            if i not in curr.child:
                return False
            curr = curr.child[i]
        return curr.end == True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for i in prefix:
            if i not in curr.child:
                return False
            curr = curr.child[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)