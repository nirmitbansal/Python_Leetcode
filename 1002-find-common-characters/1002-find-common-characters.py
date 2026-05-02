from collections import Counter

class Solution:
    def commonChars(self, words):
        count = Counter(words[0])   # frequency of first word
        
        for word in words[1:]:
            curr = Counter(word)
            for ch in count:
                count[ch] = min(count[ch], curr[ch])
        
        result = []
        for ch in count:
            result.extend([ch] * count[ch])
        
        return result