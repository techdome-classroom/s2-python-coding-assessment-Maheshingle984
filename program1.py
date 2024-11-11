



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Mapping of closing brackets to their respective opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                # Pop the topmost element if the stack is not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for the closing bracket doesn't match the stack's top element, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets are closed properly
        return not stack




  

