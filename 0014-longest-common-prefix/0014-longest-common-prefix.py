class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_lgth=float("inf")
        for s in strs:
            if len(s)<min_lgth:
                min_lgth=len(s)
        
        i=0
        while i<min_lgth:
            for s in strs:
                if s[i]!=strs[0][i]:
                    return s[:i]
            i+=1
        return s[:i]

        