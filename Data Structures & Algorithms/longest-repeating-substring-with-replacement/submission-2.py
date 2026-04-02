class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}
        start = 0
        end = 0
        res = 0

        frequencies[s[start]] = 1
        maxf = s[start]

        while end < len(s):
            # Extend window to the right by 1. Update the frequency of the newly encountered
            # character
            end += 1
            if end == len(s):
                break
            
            if s[end] not in frequencies:
                frequencies[s[end]] = 0
            frequencies[s[end]] += 1

            # Update maxf if needed, by comparing its frequency to the newly encountered 
            # character's frequency
            if frequencies[s[end]] > frequencies[maxf]:
                maxf = s[end]

            # Check if current window is valid. If not, we move the start of the window up by 1
            window_len = end - start + 1
            num_replacements = window_len - frequencies[maxf]
            if num_replacements > k:
                frequencies[s[start]] -= 1
                start += 1
                maxf = max(frequencies, key=frequencies.get)

            res = max(res, end-start+1)

        return res






        