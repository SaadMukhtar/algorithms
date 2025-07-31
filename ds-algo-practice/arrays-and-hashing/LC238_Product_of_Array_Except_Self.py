class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefixProducts = []
        suffixProducts = []
        product = 1
        for i, n in enumerate(nums):
            product *= n
            prefixProducts.append(product)
        product = 1
        for i, n in enumerate(nums[::-1]):
            product *= n
            suffixProducts.append(product)
        suffixProducts = suffixProducts[::-1]
        res = []
        for i in range(len(nums)):
            prefixProduct = prefixProducts[i-1] if i >= 1 else 1
            suffixProduct = suffixProducts[i+1] if i < len(nums)-1 else 1
            res.append(prefixProduct * suffixProduct)
        return res