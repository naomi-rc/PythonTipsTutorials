# Instead of this
my_file = open('text.txt')
content = my_file.read()
my_file.close()
print(content)

# use with construct
# specify the mode with r, r+, w, or a and b for binary
# use io.open to specify encoding type
import io

with io.open('text.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
