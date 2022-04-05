import os
import json

path = 'C:\\Yield\\AgIntegrated'
files = []
for r, d, f in os.walk(path):
	for file in f:
		if '.json' in file:
			files.append(os.path.join(r,file))
	
for f in files:
        json.loads(['MonitorName'])
        if 'Corn' in file:
            print('Corn')
        else:
            print(file,'NotCorn')
    
                











    #print(f, file=open('C:\\_Output\\DBF.txt', 'a+'))
