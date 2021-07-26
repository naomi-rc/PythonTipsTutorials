from collections import defaultdict, OrderedDict, Counter, deque, namedtuple
from enum import Enum
import json

# defaultdict : no need to check whether a key exists
mydefaultdict = defaultdict(list)
mylist = (("1","hello"), ("2","there"))

print(json.dumps(mydefaultdict))
mydefaultdict['1'] = 'hello'
mydefaultdict['2'].append('there')
mydefaultdict['2'].append('friend')
print(json.dumps(mydefaultdict))
print(json.dumps(mydefaultdict.get('2')))
print(json.dumps(mydefaultdict.get('3')))


# ordereddict : sorts according to how it was initialized
myordereddict = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in myordereddict.items():
    print(key, value)

# counter : count occurrences of an item
mylist = "hello my baby, hello my darling"
occurrences = Counter(letter for letter in mylist)
print(f"Occurrences of h: {occurrences}")
print(f"Occurrences of h: {occurrences['h']}")

with open("text.txt") as file:
    lines = Counter(file)
    print(lines)



#dequeue : a double-ended queue 
q = deque(range(5), maxlen=9)
print(q)
q.append(7)
q.extend([7])
q.extendleft([8])
q.appendleft(8)
print(q)
q.append(7) #pops out the element at the other side since maxlen=9
print(q)
q.pop()
q.popleft()
print(q)


#namedtuple : like immutable dictionnaries but faster than dictionnaries, lightweight, no more memory than regular tuples
my_named_tuple = namedtuple('TupleName', 'tuple field names')
my_tuple = my_named_tuple(tuple='hi', field='there', names='friend')

print(my_named_tuple)
print(my_tuple[0])
print(my_tuple.field)
print(my_tuple._asdict())


# Enum : enumerated named types for better organization
class Languages(Enum):
    java = 1
    javascript = 2
    typescript = 3
    python = 4
    csharp = 5

    #alias
    TypeScript = 3

print(Languages.typescript)
print(Languages.TypeScript)

print(Languages.typescript == Languages(3))
print(Languages.TypeScript == Languages(3))
print(Languages.TypeScript == Languages.typescript)

my_tuple = my_named_tuple(tuple=Languages.java, field=Languages['javascript'], names=Languages(4))
print(my_tuple)