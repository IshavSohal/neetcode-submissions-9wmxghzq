class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        prefix = 1
        for i in range(0, n):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(n-1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]

        return output
        
        