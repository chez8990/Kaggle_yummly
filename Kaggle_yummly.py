import json
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

cuisine_id = []
cusine = []
ingredients = []

with open('train.json') as f:
	data = json.load(f)
	for i in data:
		cuisine_id.append(i['id'])
		cusine.append(i['cuisine'])
		ingredients.append(i['ingredients'])

train = pd.DataFrame({'Cuisine_id':cuisine_id, 'Cuisine': cusine, 'Ingredients': ingredients})
# train.to_csv('train.csv')

def ifinlist(row, x):
    if x in row:
        return True
    else:
        return False

print train[train['Ingredients'].apply(lambda x: 'salt' in x)]['Cuisine'].value_counts(sort=False)
print train[train['Ingredients'].apply(lambda x: 'ground cumin' in x)]['Cuisine'].value_counts(sort=False, dropna= False)

