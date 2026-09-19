class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        pairs = sorted(counter.items(), key=lambda pair: pair[1], reverse=True)
        return [num for num, count in pairs[:k]]
