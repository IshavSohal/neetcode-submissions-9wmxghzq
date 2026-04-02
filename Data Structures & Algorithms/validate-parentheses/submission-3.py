class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ["{", "[", "("]
        stack = []

        for i in range(0, len(s)):
            if s[i] in open_brackets:
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                if (s[i] == "]" and stack[-1] == "[") or (s[i] == "}" and stack[-1] == "{") or (s[i] == ")" and stack[-1] == "("):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
        