class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (high + low)//2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                if nums[mid] >= nums[low] and nums[mid] > nums[high]:
                    if target >= nums[low]:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] >= nums[low] and nums[mid] < nums[high]:
                    high = mid - 1
                elif nums[mid] < nums[low] and nums[mid] < nums[high]:
                    high = mid - 1

            else: # if nums[mid] < target
                if nums[mid] >= nums[low] and nums[mid] > nums[high]:
                    low = mid + 1
                elif nums[mid] >= nums[low] and nums[mid] < nums[high]:
                    low = mid + 1
                elif nums[mid] < nums[low] and nums[mid] < nums[high]:
                    if target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1

        mid = (high + low)//2
        if nums[mid] == target:
            return mid
        return -1
        