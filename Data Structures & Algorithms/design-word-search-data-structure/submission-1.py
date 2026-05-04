class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(root, rootval, word, i ):
            if rootval == None or rootval == word[i] or word[i] == ".":
                if i == len(word) - 1:
                    return root.is_end
                return any(dfs(child, childval, word, i+1) for childval, child in root.children.items())
            return False
        return dfs(self.root, None, word, -1)