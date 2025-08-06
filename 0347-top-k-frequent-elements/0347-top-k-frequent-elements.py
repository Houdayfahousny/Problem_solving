class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]
        for num in nums :
            count[num]=1+count.get(num,0)
        for i , c in count.items():
            freq[c].append(i)
        TopK=[]
        for n in range(len(freq)-1,0,-1):
            for num in freq[n]:
                TopK.append(num)
                if len(TopK)==k:
                    return TopK

       

       