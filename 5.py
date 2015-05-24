import os
import pickle
import pprint


DATA_FILE = 'banner.p'
DATA_DIR = 'data'


root_dir = os.path.dirname(__file__)
data_filepath = os.path.abspath(
    os.path.join(root_dir, DATA_DIR, DATA_FILE))
print data_filepath
data = pickle.load(open(data_filepath, "rb") )

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

for item in data:
    output = ''
    for char, count in item:
	output = output + (char * count)
    print output


