import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operandStack = []
        operators = "+-*/"

        for t in tokens:
            print(operandStack)
            if t in operators:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()

                if t == "+":
                    operandStack.append(operand1 + operand2)
                elif t == "-":
                    operandStack.append(operand1 - operand2)
                elif t == "*":
                    operandStack.append(operand1 * operand2)
                else:
                    operandStack.append(int(str(operand1 / operand2).split('.')[0]))
                
            else:
                operandStack.append(int(t))

        return operandStack.pop()
        