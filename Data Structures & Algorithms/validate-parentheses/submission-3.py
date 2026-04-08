class Solution:
    def isValid(self, s: str) -> bool:
        ctp = {')': '(', "]" : "[", "}" : "{" }
        stack = []

        for c in s:
            if c in ctp:
                if stack and stack[-1] == ctp[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        return True if not stack else False
        
            




