class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if endWord not in wordList:
        #     return 0
        # nei = collections.defaultdict(list)
        # wordList.append(beginWord)
        # for w in wordList:
        #     for j in range(len(w)):
        #         pattern = w[:j] + "*" + w[j + 1:]
        #         nei[pattern].append(w)
        # visit = set([beginWord])
        # q = deque([beginWord])
        # res = 1
        # while q:
        #     for i in range(len(q)):
        #         word = q.popleft()
        #         if word == endWord:
        #             return res
        #         for j in range(len(word)):
        #             pattern = word[:j] + "*" + word[j+1:]
        #             for neiWord in nei[pattern]:
        #                 visit.add(neiWord)
        #                 q.append(neiWord)
        #     res += 1
        # return 0

        if endWord not in wordList or beginWord == endWord:
            return 0
        m = len(wordList[0])
        wordSet = set(wordList)
        qb, qe = deque([beginWord]), deque([endWord])
        fromBegin, fromEnd = {beginWord: 1}, {endWord: 1}

        while qb and qe:
            if len(qb) > len(qe):
                qb, qe = qe, qb
                fromBegin, fromEnd = fromEnd, fromBegin
            for _ in range(len(qb)):
                word = qb.popleft()
                steps = fromBegin[word]
                for i in range(m):
                    for c in range(97, 123):
                        if chr(c) == word[i]:
                            continue
                        nei = word[:i] + chr(c) + word[i + 1:]
                        if nei not in wordSet:
                            continue
                        if nei in fromEnd:
                            return steps + fromEnd[nei]
                        if nei not in fromBegin:
                            fromBegin[nei] = steps + 1
                            qb.append(nei)
        return 0


 









        