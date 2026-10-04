class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        prefix=1
        for i in range(n):
            ans[i]=prefix
            prefix=prefix*nums[i]
        postfix=1
        for i in range(n-1,-1,-1):
            ans[i]*=postfix
            postfix=postfix*nums[i]

        return ans
#prefix = [1,2,8,48]

# intial [1,2,4,6]
# prefix [1,1,2,8]
# postfix [48,24,6,1]