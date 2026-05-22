class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len) # this will sort the words arr by len of characters
        res = []

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break

        return res