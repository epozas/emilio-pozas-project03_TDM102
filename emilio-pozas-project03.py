import os
len(os.listdir('/anvil/projects/tdm/data/noaa/'))#Help from videos

import pandas as pd
from pathlib import Path
myfiles=[]
for year in range (1880, 1884):
    file= Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myfiles.append(file)
print(myfiles)
myfiles = [ Path(f'/anvil/projects/tdm/data/noaa/{year}.csv') for year in range (1880,1884)]
print(myfiles)

with open('/anvil/projects/tdm/data/noaa/1880.csv',"r") as f:
    mycount = 0
    for line in f:
        mycount += 1
print(f'There are {mycount} records in the file called {file}')
count = 0
for x in myfiles:
    with open(x,"r") as f:
        count += mycount
        mycount = 0
        for line in f:
            mycount += 1
files = len(myfiles)
print(f'There are {count} records in the {files} files altogether')
#Added another counter that doesn't restart in the for loop. Although it would have to be restarted if we want to run the loop with more files

mydataframes = [pd.read_csv(myfiles[x],names = ["id","date","element_code","value","mflag","qflag","sflag","obstime"]) for x in range(0,4)]
print(mydataframes)
for i in range(0,4):
    print(mydataframes[i].columns) #Tried not using print. Did not work inside of the for loop
    
for mydf in mydataframes:
    print(mydf['element_code'].unique())
for mydf in mydataframes:
    print(mydf[mydf['element_code'] == "SNOW"].size)
    
import pandas as pd
from pathlib import Path
myfiles=[]
for year in range (1880, 1884):
    file= Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myfiles.append(file)
count = 0
for file in myfiles:
    for myDF in pd.read_csv(file,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"],chunksize =10000):
        count += len(myDF[myDF['element_code'] == 'SNOW'])

print(count)
count = 0
for file in myfiles:
    for myDF in pd.read_csv(file,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"],chunksize =10000):
        for index, row in myDF.iterrows():
            if row['element_code'] == 'SNOW':
                count += 1

print(count)