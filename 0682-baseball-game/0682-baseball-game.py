class Solution:
    def calPoints(self, operations: List[str]) -> int:
        L=['+','D','C']
        stack=[]
        for i in range(len(operations)):
            if operations[i] not in L:
                stack.append(int(operations[i] ))


            elif operations[i] =='+':
                stack.append(stack[-1]+stack[-2])

            elif operations[i] =='D':
                stack.append(stack[-1]*2)

            elif operations[i] == 'C':
                stack.pop()

        return sum(stack)

        