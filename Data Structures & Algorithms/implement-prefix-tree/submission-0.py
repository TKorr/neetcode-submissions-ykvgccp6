import string

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for idx in range(len(word)):
            char = word[idx]
            if not curr.child[char]:
                curr.child[char] = Node()
            curr = curr.child[char]
        curr.end_of_word = True


    def search(self, word: str) -> bool:
        curr = self.root
        for idx in range(len(word)):
            char = word[idx]
            if not curr.child[char]:
                return False
            curr = curr.child[char]
        
        return curr.end_of_word


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for idx in range(len(prefix)):
            char = prefix[idx]
            if not curr.child[char]:
                return False
            curr = curr.child[char]
        
        return True

class Node:
    def __init__(self):
        self.child = defaultdict(str)
        self.end_of_word = False




