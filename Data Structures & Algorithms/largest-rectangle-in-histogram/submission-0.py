class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)

        for i in range(n):
            height = heights[i]
            width = 1

            j = i+1
            while j < n and heights[j] >= height:
                width += 1
                j += 1

            j = i-1
            while j >= 0 and heights[j] >= height:
                width +=1 
                j -= 1
            
            curr_area = height * width
            if curr_area > max_area:
                max_area = curr_area

        return max_area

        
        
        