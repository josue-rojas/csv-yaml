import yaml
import os
import csv
import urllib2 # i used for online csv
import getopt
import sys
# https://stackoverflow.com/questions/16283799/how-to-read-a-csv-file-from-a-url-with-python

root = os.getcwd()

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

def usage():
    # write instructions....
    print 'help is ummm.....'

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:o:u', ['help', 'input=','output=', 'url'])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    csvFile = None
    output = None
    url = False
    if len(opts) == 0:
        localCSV()
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-i', '--input'):
            csvFile = a
        elif o in ('-o', '--output'):
            output = a
        elif o in ('-u', '--url'):
            url = True
        else:
            print 'unhandled option'
    if url:
        urlCSV(csvFile, output)
    output = output if output else root+'/'+(csvFile.split('/')[-1].replace('.csv','.yml'))
    with open(csvFile, 'rb') as csvFile:
        csvToYaml(csvFile, output)


if __name__ == "__main__":
    main()
