
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        nei = defaultdict(list)

        for word in wordList:
            for c in range(len(word)):
                pattern = word[:c] + "*" + word[c+1:]
                nei[pattern].append(word)

        res = 1
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        while  q:
            for _ in range(len(q)):    
                word = q.popleft()
                if word == endWord:
                    return res
                for c in range(len(word)):
                    pattern = word[:c] + "*" + word[c+1:]
                    for adjWord in nei[pattern]:
                        if adjWord not in visited:
                            q.append(adjWord)
                            visited.add(adjWord)
            res+=1
        return 0

