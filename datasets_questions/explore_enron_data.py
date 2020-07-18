#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print len(enron_data) #146
print type(enron_data) # Its a dictionary
print enron_data['METTS MARK'] # Lets check 1st entry
print len(enron_data['METTS MARK']) #features: 21

# How many POI's are there?? (18)
cnt=0
for key in enron_data.keys():
    if enron_data[key]['poi']:
        cnt=cnt+1
print cnt

print enron_data['PRENTICE JAMES']['total_stock_value']
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

#for key in enron_data.keys():
#    print key

print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']

sal_cnt = email_cnt = 0
for key in enron_data.keys():
    if enron_data[key]['salary']!='NaN':
        sal_cnt = sal_cnt+1
    if enron_data[key]['email_address']!='NaN':
        email_cnt = email_cnt+1
print sal_cnt
print email_cnt

cnt_tp=0
for key in enron_data.keys():
    if enron_data[key]['total_payments']=='NaN':
        cnt_tp = cnt_tp+1

print cnt_tp


cnt_poi=0
for key in enron_data.keys():
    if enron_data[key]['poi']:
        if enron_data[key]['total_payments']=='NaN':
            cnt_poi=cnt_poi+1
print cnt_poi
