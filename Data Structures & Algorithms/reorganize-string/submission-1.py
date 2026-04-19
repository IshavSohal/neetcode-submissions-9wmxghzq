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
  
        #sorted_keys = sorted(freqs, key=freqs.get)[::-1] # O(nlogn) steps, where n is the number of unique letters
        heap = [(-freq, char) for char, freq in freqs.items()]
        heapq.heapify(heap)
        
        if len(heap) <= 1:
            return ""

        while True:
            most_freq = heapq.heappop(heap)
            # print("")
            # print("heap: ", heap)
            # print(res)

            if most_freq[0] == 0:
                return res

            if res == "" or most_freq[1] != res[-1]:
                res += most_freq[1]
                freqs[most_freq[1]] -= 1
            else:
                # If there is at least one more instance of the most frequent letter left, and no more
                # of the other letters, then a repetition will occur
                second_freq = heapq.heappop(heap)

                if second_freq[0] == 0:
                    return ""
                else:
                    res += second_freq[1]
                    freqs[second_freq[1]] -= 1

            heap = [(-freq, char) for char, freq in freqs.items()]
            heapq.heapify(heap)
        