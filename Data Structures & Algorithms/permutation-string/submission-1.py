class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Initialize s1 histogram
        s1_hist = {}
        for char in s1:
            if char not in s1_hist:
                s1_hist[char] = 0
            s1_hist[char] += 1

        start = 0
        end = len(s1) - 1
        s2_hist = {}

        # Intialize s2 histogram
        for char in s2[0:len(s1)]:
            if char not in s2_hist:
                s2_hist[char] = 0
            s2_hist[char] += 1

        while end < len(s2):
            is_perm = True

            # Check if current window is a permutation of s1
            for char in s1_hist:
                if char not in s2_hist or s1_hist[char] != s2_hist[char]:
                    is_perm = False
                    break
            
            if is_perm:
                return True

            # If not we proceed. Window side remains fixed. Update the s2 histogram accordingly
            s2_hist[s2[start]] -= 1
            start += 1
            end += 1
            if end < len(s2):
                if s2[end] not in s2_hist:
                    s2_hist[s2[end]] = 0
                s2_hist[s2[end]] += 1


        return False
            