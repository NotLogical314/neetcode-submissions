class TrieNode():
    def __init__(self):
        self.dct = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.dct:
                node.dct[char] = TrieNode()

            node = node.dct[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.dct:
                return False
            node = node.dct[char]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.dct:
                return False
            node = node.dct[char]
        return True
