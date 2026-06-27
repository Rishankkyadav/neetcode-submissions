class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cls = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in cls:
                if stack and stack[-1] == cls[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)    
        return True if not stack else False    




