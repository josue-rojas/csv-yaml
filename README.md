# csv-yaml
a script to convert csv to yaml files using PyYaml for use in Jekyll templating among other things

### Need
- [PyYaml](http://pyyaml.org/wiki/PyYAMLDocumentation)
- I am also using mac. (if that makes a difference (I never tested on windows))

#### Usage

Note: Use convert.py for python 2.7 and convert3.py for python 3.
```bash
Usage:
# -i --input: path/link of file (if link use url flag)
# -o --output: path name of output, if left out will convert in this folder using its name as output
# -u --url: url flag indicating input is a url and should be treated as such
# -f --folder: flag indicating input is directory/folder and should be treate as such
# -h --help: print this/help stuff.....


#Assuming using this in your working directory

# simple local file input output
python convert.py -i some/file/csvFile.csv -o some/file/converted.yml
# using url
python convert3.py -i 'http://winterolympicsmedals.com/medals.csv' -o some/file/path/converted.yml -u
# all from folder
python convert.py -i some/file/path/ -f
# all from this folder
python convert.py

```
