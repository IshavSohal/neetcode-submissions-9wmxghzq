class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        end = 1
        n = len(s)

        if n == 0:
            return 0

        substring = s[0]

        while end < n:
            if s[end] not in substring:
                substring += s[end]
                end += 1
            else:
                longest = max(longest, end-start)
                start += substring.index(s[end]) + 1
                substring = s[start:end]

        longest = max(longest, end-start)
        return longest


        