class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close2open={")":"(","]":"[","}":"{"}
        for c in s:
            if c in close2open :
                if stack and stack[-1]==close2open[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        