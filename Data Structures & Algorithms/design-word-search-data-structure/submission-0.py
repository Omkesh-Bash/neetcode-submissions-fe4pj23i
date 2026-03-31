class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.isEnd = False

# There will be at most 2 dots in word for search queries.

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.childrens:
                curr.childrens[c] = TrieNode()
            curr = curr.childrens[c]
        curr.isEnd = True
    

    def search(self, word: str) -> bool:

        def dfs(j, curr : TrieNode):
            for i in range(j, len(word)):
                c = word[i]
                # There can only be two main cases
                if c == '.': # First main case
                    # There are total 24 possible children
                    for child in curr.childrens.values() : # check each child for possible result
                        if dfs(i+1, child): 
                            return True
                    else :
                        # After completation of loop if no True result is found which means the word is not present
                        return False


                else: # second main case
                    if c not in curr.childrens:
                        return False
                    curr = curr.childrens[c]

            # Base : if program reached to end of word
            return curr.isEnd
        
        return dfs(0, self.root)