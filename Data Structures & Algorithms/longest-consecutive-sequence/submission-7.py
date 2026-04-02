class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        largest = 0

        for num in nums_set:
            if (num-1) not in nums_set:
                sequence = [num]
                next_num = num+1
                length = 1
                while next_num in nums_set:
                    sequence.append(next_num)
                    next_num += 1
                    length += 1
                largest = max(largest, length)

        return largest
        
