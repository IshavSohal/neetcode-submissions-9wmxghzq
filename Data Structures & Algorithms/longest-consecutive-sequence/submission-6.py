class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sequences = {}

        for num in nums:
            if (num-1) not in nums_set and (num-1) not in sequences:
                sequences[num] = [num]

        for start in sequences:
            # use a while loop to continuously add values to the current seq, until there
            # are no more to add
            num = start+1
            while num in nums_set:
                sequences[start].append(num)
                num += 1

        print(sequences)

        if(len(sequences) == 0):
            return 0

        return len(sequences[max(sequences, key=lambda k: len(sequences[k]))])
        
