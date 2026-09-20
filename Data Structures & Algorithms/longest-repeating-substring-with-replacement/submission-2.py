class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left, maxFreq, best = 0,0,0

        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i],0) + 1
            maxFreq = max(maxFreq, counts[s[i]])

            while (i - left + 1) - maxFreq > k:
                counts[s[left]] -= 1
                left += 1
            
            best = max(best, i - left + 1)
        
        return best