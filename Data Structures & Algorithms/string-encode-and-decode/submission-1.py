class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for s in strs:
            string += str(len(s))
            string += "#"
            string += s

        return string

    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            number = int(s[i:j])
            strs.append(s[j+1:j+1+number])

            i = j+1+number
        
        return strs


