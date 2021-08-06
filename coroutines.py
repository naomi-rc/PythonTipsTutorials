# coroutines : data consumers (as opposed to data producers like generators); consumes sequences

def find_in_file(content):
    value = (yield) # yield returns whatever value we give to send()
    for line in content.readlines():        
        if value.lower() in line.lower():
            print(line.lower().replace(value, value.upper()))

my_coroutine = find_in_file(open("text.txt", "r")) # returns a gnereator object - the coroutine
print(type(my_coroutine)) # <class 'generator'>
next(my_coroutine) #starts the coroutine to move position to first yield expression - can also use .send(None) or use a decorator

try:
    my_coroutine.send("of")
except:
    print("END OF SEARCH")
    my_coroutine.close() # closes the coroutine
