# Keyword 'global' makes a variable accessible globally, outside of its current scope (if in a method for example) 
# Best not to use 'global' in practical programming

# You can return multiple values at once in python (returned as a tuple)

def global_and_return(x, y):
    global resultA
    global resultB
    resultA = x + y
    resultB = x - y
    return resultA, resultB


print(f"Multiple return: {global_and_return(5,4)}") 
print(f"Global variables: {resultA} and {resultB}") # Have to have run the function first
