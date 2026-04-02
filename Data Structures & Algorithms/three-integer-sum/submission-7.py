class Solution:
    def twoPointer(self, arr, target):
        print('twopointer')
        i = 0
        j = len(arr) - 1
        res = []
        encountered = set()

        while i < j:
            print('i and j')
            print(i)
            print(j)
            currSum = arr[i] + arr[j]

            if currSum == target:
                print('target found')
                if (arr[i], arr[j]) not in encountered and (arr[j], arr[i]) not in encountered:
                    res.append([arr[i], arr[j]])

                encountered.add((arr[i], arr[j]))
                i += 1

            elif currSum > target:
                print('move j')
                j -= 1

            else:
                print('move i')            
                i += 1

        return res


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        triplets = [] # helps to avoid duplicates, convert to array at end

        n = len(nums)
        i = 0


        while i < n:
            print('i in nums_sorted')
            print(i)
            target = -nums_sorted[i]
            pairs = self.twoPointer(nums_sorted[i+1:], target)

            for pair in pairs:
                triplet = pair + [nums_sorted[i]]
                triplets.append(triplet)

            while i+1 < n and nums_sorted[i] == nums_sorted[i+1]:
                i += 1
            i += 1

                
        return triplets





        