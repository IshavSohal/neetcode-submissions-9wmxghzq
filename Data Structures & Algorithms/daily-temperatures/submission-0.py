class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = [] # stack will be ordered least to greatest at all times

        for i in range(n):
            curr_temp = temperatures[i]
            
            while len(stack) > 0 and stack[-1][0] < curr_temp:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            stack.append((curr_temp, i))

        return result
        