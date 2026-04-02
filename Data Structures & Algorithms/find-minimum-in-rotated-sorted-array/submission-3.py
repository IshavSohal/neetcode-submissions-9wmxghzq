class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2

        while low <= high:
            mid = (high + low) // 2

            if low == high:
                return nums[mid]
            
            if nums[mid] >= nums[low] and nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] >= nums[low] and nums[mid] < nums[high]:
                high = mid - 1
            elif nums[mid] < nums[low] and nums[mid] < nums[high]:
                high = mid
                

        return nums[mid]

        