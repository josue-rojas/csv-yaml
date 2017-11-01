import yaml
import os
import csv
import urllib2 # i used for sheets online csv
# https://stackoverflow.com/questions/16283799/how-to-read-a-csv-file-from-a-url-with-python

root = os.getcwd()

 https://docs.google.com/spreadsheets/d/11vOfFXB8uQ0te-5yZ16CWFUQM6ZoJzpouhTBHUhFyAw/export?format=csv&id=11vOfFXB8uQ0te-5yZ16CWFUQM6ZoJzpouhTBHUhFyAw&gid=0

#
# takes a csvFile name and output file name/path
def csvToYaml(csvFile, output):
    stream = file(output, 'w')
    csvOpen = csv.reader(csvFile)
    keys = next(csvOpen)
    for row in csvOpen:
        yaml.dump([dict(zip(keys, row))], stream, default_flow_style=False)

def urlCSV(url, output=None):
    csvFile = urllib2.urlopen(url)
    output = output if output else root+'/'+(url.split('/')[-1].replace('.csv','.yml'))
    csvToYaml(csvFile, output)

def localCSV():
    for f in os.listdir(root):
        if f.endswith('.csv'):
            csvFile = os.path.join(root, f)
            with open(csvFile, 'rb') as csvfile:
                output = f.replace('.csv','.yml')
                csvToYaml(csvfile, output)


urlCSV('https://docs.google.com/spreadsheets/d/11vOfFXB8uQ0te-5yZ16CWFUQM6ZoJzpouhTBHUhFyAw/export?format=csv&id=11vOfFXB8uQ0te-5yZ16CWFUQM6ZoJzpouhTBHUhFyAw&gid=0')
