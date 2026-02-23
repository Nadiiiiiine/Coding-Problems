def romanToInt(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev = 0
    
    # Process from the end: if a smaller value appears before a larger, subtract it Otherwise, we add it.
    for ch in reversed(s):
        curr = roman[ch]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
        
    return total

# Complexity
# Time: O(n) 
# Space: O(1)
