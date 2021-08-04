# for else : for loop with else statement
# when the for loop ends normally without encountering a break statement, the else block is run

for i in range(1, 6):
    print(f"Printing {i}")
else:
    print("Finished printing")


for i in range(1, 6):
    if i == 4:
        break;
    print(f"Printing {i}")    
else:
    print("This will never print")