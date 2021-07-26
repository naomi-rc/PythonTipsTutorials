#args* and kwargs**: pass unspecified number of arguments to a function
#args*: for non-keyworded variable length argument list
#kwargs**: for keyworded/named variable length arguments
# func(*args, **kwargs) therefore is to accept all possible arguments
def test_args(arg1, *args):
    print(f"arg1: {arg1}")
    for arg in args:
        print(f"another arg: {arg}")

def test_kargs(**kwargs):
    for key, value in kwargs.items():
        print(f"Key: {key} - Value: {value}")

test_args("Hello", "my", "friend")
print("\n")
test_kargs(arg1="Hello", arg2 = "my", arg3 = "friend")