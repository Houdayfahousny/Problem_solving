class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            
            nums[i]=nums[i]**2
            output.append(nums[i])

        output.sort()
        return output




        