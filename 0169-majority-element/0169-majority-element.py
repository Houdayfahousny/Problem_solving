class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter=defaultdict(int)
        n=len(nums)
        res=0

        for m in nums:
            counter[m]+=1
         
        for i , c in counter.items():
            if c > n//2:
                return i

                