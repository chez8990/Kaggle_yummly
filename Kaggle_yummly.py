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



ingre = pd.read_csv('ingre.csv', index_col=None)


ingre_sort_count = ingre.sort_values('count', ascending = False)
top_40_ingre = ingre_sort_count[:40]

cuisine_list = np.unique(train['Cuisine'])

def cuisin_ingredients(cuisine_type, top_num=10):
	dish = train[train['Cuisine']==cuisine_type]['Ingredients']
	combined = np.unique(reduce(lambda x,y: x+y, dish), return_counts=True)
	top_count = [x for (y,x) in sorted(zip(combined[1], combined[0]))]
	return top_count[:top_num]
print cuisin_ingredients('russian')
