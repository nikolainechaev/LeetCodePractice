class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)
        pointer1 = 0
        pointer2 = 0
        results = []
        
        while pointer1 < length1 or pointer2 < length2:
            if pointer1 < length1:
                results.append(word1[pointer1])
                pointer1 += 1
            if pointer2 < length2:
                results.append(word2[pointer2])
                pointer2 += 1
        finalStr = ''.join(results)
        return finalStr