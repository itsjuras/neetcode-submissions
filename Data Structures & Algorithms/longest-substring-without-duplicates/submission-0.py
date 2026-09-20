class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLength = 0
        length = 0
        left = 0

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                length += 1
            else:
                while s[left] != s[i]:
                    seen.discard(s[left])
                    left += 1
                    length -= 1
                left += 1
            
            maxLength = max(maxLength, length)

        return maxLength
                
