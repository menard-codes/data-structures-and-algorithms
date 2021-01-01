
def bitStrings(n):
    if n == 0:
        return []
    if n == 1:
        return ["O", "1"]
    return [digit+bitstring for digit in bitStrings(1) for bitstring in bitStrings(n - 1)]


print(bitStrings(3))

"""
bitStrings(3)
n = 3

    bitStrings(1)
        ['0', '1'] for each digit        
    digit = 0
    
    bitStrings(2)
    n = 2
        
        bitStrings(1)
            ['0', '1'] for each digit
        digit = 0
        
        bitStrings(1)
            ['0', '1'] for each (inner for loop)
        
        # [00]
        # [00, 01]
        
        digit = 1
        
        bitStrings(1)
            ['0', '1'] for each inner
        
        # [00, 01, 10]
        # [00, 01, 10, 11]
    return [00, 01, 10, 11]
    
    # [000, 001, 010, 011]
    # [000, 001, 010, 011, 100, 101, 110, 111]

return [000, 001, 010, 011, 100, 101, 110, 111]


DO THE CALL STACK LATER!!!!!
"""
