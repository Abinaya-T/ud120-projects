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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

len_d = len(enron_data)
print "data points (people) present in the dataset:" , len_d
len_f = len(enron_data.values()[0])
print "features available for each person in the dataset:" , len_f


pois = 0
for i in enron_data.values():
 if i['poi'] == True:
  pois += 1
print "The number of persons of interest in the dataset:", pois

poi_names = open("H:\\ML-Projects\\ud120-projects\\final_project\\poi_names.txt", "r")
poi = poi_names.readlines()
count = len(poi[2:])
print "Total no of Pois overall:", count

p_stock = enron_data["PRENTICE JAMES"]["total_stock_value"]
print "total value of the stock belonging to James Prentice:", p_stock

no_mail = enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print " No of email messages from Wesley Colwell to persons of interest:", no_mail

s_stock = enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print "the value of stock options exercised by Jeffrey K Skilling:", s_stock