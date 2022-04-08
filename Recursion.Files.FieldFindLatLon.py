import os
import json

path = 'C:\\Users\\LundbladeA\\Reed Elsevier Group ICO Reed Elsevier Inc\\OG-ProAM agX - Product - Troubleshooting\\HeartlandSoilSampling\\2022-04-08\\LargeExtentsPatrickQuarter\\EarlyOutQA\\Extract'
filelist = []
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            filelist.append(os.path.join(r, file))

for f in filelist:
    if "Quarter" in f:
        print(f, '        Quarter')
    else:
        print(f, 'NotQuarter')

# print(f, files=open('C:\\_Output\\DBF.txt', 'a+'))
# https://docs.python.org/3.6/library/pathlib.html#module-pathlib path manipulation stuff
