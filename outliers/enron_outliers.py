#!/usr/bin/python
import numpy as np
import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.title("Scatter-plot with outlier")
matplotlib.pyplot.show()

# spoted the outlier what is that point.
print type(data)
# What is the maximum value of a bonus which is an outlier point
max_bonus = max(data[:,1])
print max_bonus # 97343619.0

# in the data dictionary find the entry for which bonus is 97343619.0
for key in data_dict.keys():
    if data_dict[key]['bonus'] == 97343619:
        print key
        print data_dict[key]
        break

data_dict.pop( "TOTAL", 0 )
data = featureFormat(data_dict, features)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.title("Scatter-plot without outlier")
matplotlib.pyplot.show()

for x,y in data:
    if x>1000000 and y>5000000:
        print (x,y)

# What are the keys for which (salary and bonus) are:
#(1072321.0, 7000000.0)
# (1111258.0, 5600000.0)

for key in data_dict.keys():
    if data_dict[key]['salary'] in [1072321,1111258] and data_dict[key]['bonus'] in [7000000,5600000]:
        print key
    
