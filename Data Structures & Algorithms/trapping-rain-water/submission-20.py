class Solution:

    def find_k(self, height, start, end):
        k = float('inf')
        k_index = 0

        for i in range(end-1, start-1,-1):
            if height[i] > height[end]:
                k = height[i]
                k_index = i
                return {"k": k, "index": k_index, "bars_between": sum(height[k_index+1:end])}


    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        i = 0
        j = min(1, n - 1)
        bars_between = 0 
        area_counted = 0

        if n <= 1:
            return 0


        while i < n and j < n:
            if height[i] > 0:
                if height[j] > 0:
                    if height[i] > height[j]:

                        # if the height of the bar at j has increased, we have found a pocket of area
                        # this assumes that all bars between i and j are less/equal to the bar at j
                        # We need to find the smallest bar between i and j which is greater than the bar 
                        # at j
                        # We need to compute the bars_between value for j and k in particular
                        # We need to compute the area_counted value for j and k in particular
                        if height[j] > height[j-1]:
                            k_info = self.find_k(height, i, j)
                            print("k_info")
                            print(k_info)
                            area = (height[j] * (j - k_info["index"] - 1)) - k_info["bars_between"] - area_counted
                            total += area
                            area_counted += area

                        bars_between += height[j]
                        j += 1
                    else:
                        # when we encounter a j that is greater than or equal to i, i must
                        # pivot. Otherwise i remains anchored
                        area = (min(height[i], height[j]) * (j - i - 1)) - bars_between - area_counted
                        total += area
                        i = j 
                        j += 1
                        bars_between = 0
                        area_counted = 0

                else:
                    j += 1
            else:
                i += 1
                if height[j] == 0 or i == j:
                    j += 1

        # while searching for a j whose height is greater than or equal to i's height, if j reaches
        # the end of the array, we must compute the remaining area from i to the end of the array
        print('i upon returning')
        print(i)
        print('area_counted upon returning')
        print(area_counted)
        print('bars_between upon returning')
        print(bars_between)
        return total



 

        