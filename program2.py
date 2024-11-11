class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to integers
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        i = 0
        
        while i < len(s):
            # If this is the last numeral or the current numeral is greater than or equal to the next one
            if i == len(s) - 1 or roman_to_int[s[i]] >= roman_to_int[s[i + 1]]:
                total += roman_to_int[s[i]]
                i += 1
            else:
                # Current numeral is less than the next one, so it's a subtractive combination
                total += roman_to_int[s[i + 1]] - roman_to_int[s[i]]
                i += 2
        
        return total


