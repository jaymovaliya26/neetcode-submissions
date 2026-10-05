class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low=0
        high=len(heights)-1
        max_area = 0
        while low<high:
            min_height = min(heights[low],heights[high])
            water = min_height*(high-low)
            max_area = max(water,max_area)
            if heights[low] < heights[high]:
                low += 1
            else:
                high-=1
        return max_area

        