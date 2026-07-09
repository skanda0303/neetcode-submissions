class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        leftprod = 1
        rightprod = 1
        maxprod = -float('inf')
        for i in nums:
            if leftprod == 0:
                leftprod = 1
            leftprod *= i
            maxprod = max(leftprod,maxprod,)

        for i in range(len(nums)-1,-1,-1):
            if rightprod == 0:
                rightprod = 1
            rightprod *= nums[i]
            maxprod = max(rightprod,maxprod,)

        return maxprod
