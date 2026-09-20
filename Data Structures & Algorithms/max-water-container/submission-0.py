class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, maxi = 0,len(heights)-1,0

        while left < right:
            area = (min(heights[left], heights[right])) * (right-left)
            if heights[left] > heights[right]:
                right -=1
            else:
                left +=1
            maxi = max(maxi, area)

        return maxi
