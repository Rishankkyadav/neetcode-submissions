class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            area = min(heights[right] , heights[left]) * (right -left )
            
            max_area = max(max_area , area)

            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
            
        if left >= right:
            return max_area
           






        