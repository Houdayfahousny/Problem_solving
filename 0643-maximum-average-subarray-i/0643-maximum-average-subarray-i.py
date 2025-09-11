class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum=curSum=sum(nums[:k])
        for i in range(k,len(nums)):
            curSum+=nums[i]-nums[i-k]
            maxSum=max(maxSum,curSum)
        return maxSum/k
            

        