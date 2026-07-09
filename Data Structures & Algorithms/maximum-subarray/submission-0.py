class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = nums[0]
        maxsum = nums[0]
        for i in range(1,len(nums)):
            if summ < 0:
                summ = 0
            summ+=nums[i]
            maxsum =  max(summ,maxsum)

        return maxsum