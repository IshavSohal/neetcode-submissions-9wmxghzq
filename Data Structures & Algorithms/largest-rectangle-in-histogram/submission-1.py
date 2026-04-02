class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        stack = []
        left_bound = {}
        right_bound = {}

        # Left-right traversal of heights array. Used to find right boundary for each bar
        for i in range(n):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                stack.pop()

            # We update the right boundary of each element  currently in the stack to the current index, `i`
            stack.append(i)
            for idx in stack:
                right_bound[idx] = i

        # Clear stack
        stack = []

        # Right-left traversal of heights array. Used to find left boundary for each bar
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                stack.pop()

            # We update the left boundary of each element  currently in the stack to the current index, `i`
            stack.append(i)
            for idx in stack:
                left_bound[idx] = i


        # Iterate through heights array and compute the area for each bar
        for i in range(n):
            height = heights[i]
            width = right_bound[i] - left_bound[i] + 1
            area = height * width

            if area > max_area:
                max_area = area

        return max_area