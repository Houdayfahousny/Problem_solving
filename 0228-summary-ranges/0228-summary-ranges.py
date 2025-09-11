class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output=[]
        if not nums:
            return output
        l=0

        for r in range(1,len(nums)+1):
            if r==len(nums) or nums[r]!=nums[r-1]+1:
                if l==r-1:
                    output.append(str(nums[l]))
                else:
                    output.append(f"{nums[l]}->{nums[r-1]}")
                l=r
        return output
            

        