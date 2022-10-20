from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        # print(count)
        return sorted(list(count.keys()), key=lambda x: (-count[x], x))[:k]