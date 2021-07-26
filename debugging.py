import pdb

def make_bread(type):
    #pdb.set_trace()
    breakpoint() #automatically imports pdb and calls pdb.set_trace()
    return "I don't have time"

print(make_bread("good"))
 
#commands: c (continue), w (current context), a (arguments), s (STEP - stop at first possible occasion), n (NEXT - reach next line in function)