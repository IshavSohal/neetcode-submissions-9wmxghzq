class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            left_height = heights[i]
            right_height = heights[j]
            height = min(left_height, right_height)
            width = j - i
            area = height * width

            if area > max_height:
                max_height = area

            if left_height <= right_height:
                i += 1
            else: 
                j -= 1
            
        return max_height



            
        