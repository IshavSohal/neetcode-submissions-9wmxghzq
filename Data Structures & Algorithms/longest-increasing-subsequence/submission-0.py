class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = {nums[0]: [nums[0]]}
        longest_global = 1

        for i in range(1, len(nums)):
            n = nums[i]
            in_mem = n in mem
            
            longest_local = 0
            if in_mem:
                longest_local = len(mem[n])
            
            longest_key = None
            new_seq = []
            
            # Iterate over keys of mem. Find all keys less than n, and choose the one
            # whose list is the longest. When found, add a new entry to mem, with key n
            # and value being the longest list found + [n]. If no such list is found (n 
            # is the smallest element encountered thus far), we add a new blank entry to mem
            for key in mem:
                if key < n:
                    if longest_local < len(mem[key])+1:
                        longest_local = len(mem[key])+1
                        longest_key = key

            # Add a new entry to mem, with key n. If entry already exist, choose longer of the two
            if longest_key != None:
                new_seq = mem[longest_key] + [n]
            else:
                new_seq = [n]
            
            if not in_mem or (in_mem and len(new_seq) > len(mem[n])):
                mem[n] = new_seq
            
            longest_global = max(longest_local, longest_global)

        return longest_global