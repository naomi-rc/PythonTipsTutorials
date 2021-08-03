# comprehensions : sequences created from sequences

# list []
print([x for x in range(10) if x%2==0]) # [0, 2, 4, 6, 8]

# dict {:}
dictionary = {'a': 1, 'b': 2, 'c':3, 'A': 27, 'B': 28, 'C': 29}
print({value : key for key, value in dictionary.items()}) # {1: 'a', 2: 'b', 3: 'c', 27: 'A', 28: 'B', 29: 'C'}
print({key.lower() : dictionary.get(key.lower(), 0) + dictionary.get(key.upper(), 0) for key in dictionary.keys()}) # {'a': 28, 'b': 30, 'c': 32}

# set {}
words = ["a", "b", "c", "abcd", "efgh", "abcdefgh"]
print({len(value) for value in words}) # {8, 1, 4}

# generator ()
generator = (x for x in range(10) if x%2==0)
print(generator)        # 0
for x in generator:     # 2
    print(x)            # 4
                        # 6
                        # 8