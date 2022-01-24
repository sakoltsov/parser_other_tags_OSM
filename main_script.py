import pandas as pd
import re

df = pd.read_csv('bq-results.csv')
df = df.set_index('osm_id')
column = dict()
column = dict.fromkeys(list(df.index))
resuls = pd.DataFrame([], index=list(df.index))

for index, rows in df.iterrows():
    for ro in rows:
        column[index] = ro.split(r'","')
        
spoof = 0

for keys,values in column.items():
    for wl in range(len(values)):
        first, two = values[wl].split(r'"=>"')
        first = first.replace(':','_')
        if r'[а-яА-ЯёЁ]' in first:
            first = re.sub(r'[а-яА-ЯёЁ]',spoof,first)
            spoof += 1
        first = re.sub(r'[^a-zA-Z0-9_]','',first)
        two = two.replace('"','')
        resuls.loc[[keys],first] = two
        
resuls.to_csv("resuls.csv")
tst = list(resuls.columns)
schema_bq = 'osm_id:integer'

for num_col in range(len(tst)):
    schema_bq = schema_bq + ',' + tst[num_col] + ':string'
    
#for save txt file    
myText = open(r'schema_bq.txt','w')
myText.write(schema_bq)
myText.close()

#for save json
import json
mySchemTXT = open(r'schema_bq.txt','r')
sch_txt = mySchemTXT.read()
mySchemTXT.close()
sch_list = list(sch_txt.split(','))
sch_dict = dict()
for x in range(len(sch_list)):
    k, v = sch_list[x].split(':')
    sch_dict[k] = v
sch_dict = json.dumps(sch_dict)
#BQ no read this :(


with open('schema_bq.json', 'w') as f:
    json.dump(sch_dict, f)
