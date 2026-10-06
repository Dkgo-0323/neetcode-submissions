class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True

        rank = {ch: i for i, ch in enumerate(order)}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j == len(w2) or rank[w1[j]] > rank[w2[j]]:
                    return False
                elif rank[w1[j]] < rank[w2[j]]:
                    break
        return True