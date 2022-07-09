class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if (b == "(" or b == "{" or b == "["):
                stack.append(b)
            else:
                if not stack:
                    return False
                lastBracket = stack.pop()
                if lastBracket == "(" and b != ")":
                    return False
                if lastBracket == "[" and b != "]":
                    return False
                if lastBracket == "{" and b != "}":
                    return False
        if not stack:
            return True
        else: 
            return False