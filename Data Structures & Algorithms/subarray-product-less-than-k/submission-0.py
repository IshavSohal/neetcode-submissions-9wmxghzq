class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        num_subarrays = 0
        curr_product = 1

        while i < n and j < n:
            if curr_product * nums[j] < k:
                num_subarrays += j - i + 1
                curr_product *= nums[j]
                j += 1
            else:
                if i == j:
                    j += 1
                else:
                    curr_product /= nums[i]

                i += 1

        return num_subarrays