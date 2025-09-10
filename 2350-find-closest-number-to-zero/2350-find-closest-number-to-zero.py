class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        output=nums[0]
        for i in range(1,len(nums)):
            if abs(nums[i])<abs(output) or (abs(nums[i])==abs(output) and nums[i]>output):
                output=nums[i]
        return output
        