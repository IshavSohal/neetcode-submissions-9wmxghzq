class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parantheses = self.recursiveParanthesis(n, n*2, [])
        return parantheses



    def recursiveParanthesis(self, n, level, stack):
        parantheses = []
        print(level - 1)

        # Need to start closing parantheses, rather than opening new ones
        if level == 1:
            return [")"]

        # if the stack is full of opening parantheses, we need to close them
        if level - 1 <= len(stack):
            
            path1Stack = stack.copy()
            if path1Stack[-1] == "(":
                path1Stack.pop()
            childParantheses1 = self.recursiveParanthesis(n, level-1, path1Stack)
            for p in childParantheses1:
                parantheses.append(")" + p)

        else: 
            if len(stack) > 0:
                # Path 1: ")"
                path1Stack = stack.copy()
                if path1Stack[-1] == "(":
                    path1Stack.pop()
                childParantheses1 = self.recursiveParanthesis(n, level-1, path1Stack)
                for p in childParantheses1:
                    parantheses.append(")" + p)

            # Path 2: "("
            path2Stack = stack.copy()
            path2Stack.append("(")
            childParantheses2 = self.recursiveParanthesis(n, level-1, path2Stack)
            for p in childParantheses2:
                parantheses.append("(" + p)

        return parantheses
            

        

        