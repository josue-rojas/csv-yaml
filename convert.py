import yaml
import os
import csv
import json
# import urllib2 # used for sheets online csv

# a = {'name': 'Silenthand Olleander', 'race': 'Human'}
# print yaml.dump({'name': 'Silenthand Olleander', 'race': 'Human'})

root = os.getcwd()


for f in os.listdir(root):
    if f.endswith('.csv'):
        csvFile = os.path.join(root, f)
        with open(csvFile, 'rb') as csvfile:
            stream = file(f.replace('.csv','.yml'), 'w')
            csvOpen = csv.reader(csvfile)
            keys = next(csvOpen)
            # data = []
            for row in csvOpen:
                # row = dict(zip(keys, row))
                # data.extend([dict(zip(keys, row))])
                # print data
                yaml.dump([dict(zip(keys, row))], stream, default_flow_style=False)
