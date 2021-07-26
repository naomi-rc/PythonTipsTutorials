# When you assign a variable to another variable and change the value, the change will be reflected by both variables
x = [5]
y = x
y[0] = 7

print(f"x: {x} and y: {y}") # Both will be arrays of [7]