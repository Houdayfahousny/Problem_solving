class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left,right=0,len(s)-1
    
        while left<=right:
            if left==right:
                break
            else:    
                tmp=s[left]
                s[left]=s[right]
                s[right]=tmp
                left+=1
                right-=1
        return s
        