import os
import json

path = 'C:\\Yield\\AgIntegrated'
files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            files.append(os.path.join(r, file))

for f in files:
    json.loads(['MonitorName'])
    if 'Corn' in files:
        print('Corn')
    else:
        print(files, 'NotCorn')

# print(f, file=open('C:\\_Output\\DBF.txt', 'a+'))
# https://docs.python.org/3.6/library/pathlib.html#module-pathlib path manipulation stuff
