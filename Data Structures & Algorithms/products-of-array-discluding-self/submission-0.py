class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = []
        suffix_product = []
        res = []
        n = len(nums)

        for i in range(0, n):
            if (len(prefix_product) == 0):
                prefix_product.append(nums[i])
            else:
                prefix_product.append(prefix_product[-1] * nums[i])
        
        print('prefix product')
        print(prefix_product)
            
        for j in range(n-1, -1, -1):
            if (len(suffix_product) == 0):
                suffix_product.append(nums[j])
            else:
                suffix_product.append(suffix_product[-1] * nums[j])

        print('suffix product')
        print(suffix_product)

        for i in range(0, len(nums)):
            if(i ==0):
                res.append(suffix_product[n - 2])
            elif(i == len(nums) - 1):
                res.append(prefix_product[n - 2])
            else:
                res.append(prefix_product[i-1] * suffix_product[n-2-i])

        return res
        
        