import os
import json

path = ''C:\\Users\\LundbladeA\\Reed Elsevier Group ICO Reed Elsevier Inc\\OG-ProAM agX - Product - Troubleshooting\\HeartlandSoilSampling\\2022-04-08\\LargeExtentsPatrickQuarter\\EarlyOutQA\\Extract''
files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            files.append(os.path.join(r, file))

for f in files:
    json.loads(['MonitorName'])
    if 'Corn' in files:
        print(files, 'Corn')
    else:
        print(files, "NotCorn")

# print(f, files=open('C:\\_Output\\DBF.txt', 'a+'))
# https://docs.python.org/3.6/library/pathlib.html#module-pathlib path manipulation stuff
