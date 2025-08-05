class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map={}
        for i , j in enumerate(nums):
            diff=target-j
            if diff in Map:
                return [Map[diff],i]
            Map[j]= i
            
        