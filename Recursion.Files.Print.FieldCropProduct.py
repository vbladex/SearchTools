import os
import json
import pandas as pd


rootdir = 'C:\\Users\\LundbladeA\\Reed Elsevier Group ICO Reed Elsevier Inc\\OG-ProAM agX - Product - Troubleshooting\\ShawnPeterson\\NutrienInnovation\\EO'
for folder, dirs, file in os.walk(rootdir):
    for files in file:
        if files.endswith('.json'):
            fullpath = open(os.path.join(folder, files), 'r')
            with open(os.path.join(folder, files)) as f:
                d = json.load(f)
                print(f, d["FieldName"])