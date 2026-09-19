class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        counter = 1
        longestCount = 0   

        sortedList = sorted(nums)

        for i in range(len(sortedList)):
            if i < len(sortedList) - 1:
                if sortedList[i] == sortedList[i+1]:
                    continue 
                elif sortedList[i] + 1 == sortedList[i+1]:
                    counter += 1
                else:
                    if longestCount < counter:
                        longestCount = counter
                    counter = 1

        if longestCount < counter:
            longestCount = counter

        return longestCount