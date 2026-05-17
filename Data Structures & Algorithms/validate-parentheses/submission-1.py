class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" : "["} # these are character combinations
        for c in s:
            if c in closeToOpen: # if character is key in the dictionary...
                if stack and stack[-1] == closeToOpen[c]: # match its corresponding closing value pair from the top of the stack.
                    stack.pop() # if match then remove the key value pair from the stack.
                else:
                    return False # return false if it is not balanced.
            else: # if closing character is not in the list then add it in dict.
                stack.append(c)
        
        return True if not stack else False
            