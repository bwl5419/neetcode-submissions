class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item in "+-/*":
                item1= stack.pop()
                item2=stack.pop()
                if item in "+":
                    stack.append(item2+item1)
                elif item in "-":
                    stack.append(item2-item1)
                elif item in "*":
                    stack.append(item2*item1)
                else:
                    stack.append(int(item2/item1))
            else:
                stack.append(int(item))

        return stack[0]

            

                
        