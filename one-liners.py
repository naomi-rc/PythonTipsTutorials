# serve a file over network in console
    # python -m http.server

# pretty print lists and dictionaries
from pprint import pprint
import os

my_dir = os.path.dirname(__file__)
pprint([filename for path, directory, filename in os.walk(my_dir)])

# print json by piping file content (cat) to python -m json.tool
    # cat myfile | python -m json.tool

# profiling scripts
    # python -m cProfile my_script.py

# csv to json
    # python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"

# flattening lists (list must be of depth 2)
import itertools
my_list = [[1, 2, 3], [4, 5, 6, 9], [10, 11, 12, [13, 14]],  [7, 8]] # [13, 14] prints as is
print(list(itertools.chain(*my_list)))
print(list(itertools.chain.from_iterable(my_list)))


# one-liner assignments for initialization 
class A(object):
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})