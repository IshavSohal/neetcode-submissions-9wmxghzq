class Solution:
    def reorganizeString(self, s: str) -> str:
        freqs = {}
        res = ""

        if len(s) == 1:
            return s

        for char in s:
            if char not in freqs:
                freqs[char] = 0
            freqs[char] += 1
  
        sorted_keys = sorted(freqs, key=freqs.get)[::-1]
        
        if len(sorted_keys) <= 1:
            return ""

        while True:
            if freqs[sorted_keys[0]] == 0:
                return res

            if res == "" or sorted_keys[0] != res[-1]:
                res += sorted_keys[0]
                freqs[sorted_keys[0]] -= 1
            else:
                # If there is at least one more instance of the most frequent letter left, and no more
                # of the other letters, then a repetition will occur
                if freqs[sorted_keys[1]] == 0:
                    return ""

                res += sorted_keys[1]
                freqs[sorted_keys[1]] -= 1

            sorted_keys = sorted(freqs, key=freqs.get)[::-1]
        