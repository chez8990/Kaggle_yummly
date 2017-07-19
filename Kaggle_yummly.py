import json
import pandas as pd
import numpy as np
import sys
import re
from sklearn.preprocessing import LabelEncoder
reload(sys)
sys.setdefaultencoding('utf-8')

# cuisine_id = []
# cuisine = []
# recipe = []
# uniqueIng =[]
# with open('train.json') as f:
# 	data = json.load(f)
# 	for i in data:
# 		cuisine_id.append(i['id'])
# 		cuisine.append(i['cuisine'])
# 		ing1 = i['ingredients']
# 		ing = map(lambda x: re.sub('\(.*\)|[^a-zA-Z\s]','' , x), ing1)
# 		ing = map(lambda x: x.replace(' ', '_'), ing)
# 		recipe.append(ing)   
# 		uniqueIng+= list(filter(lambda x: x not in uniqueIng, ing))







# IngNumber = LabelEncoder()
# IngNumber.fit(uniqueIng)
# toNumber = IngNumber.transform(uniqueIng)
# ingre_names = IngNumber.classes_

# pre_recipe=recipe

# for rec in recipe:
# 	rec = IngNumber.transform(rec)


# data_save = {'Recipe': pre_recipe, 'RecipeClass': recipe, 'Unqiue ingredients': ingre_names, 'Cuisine': cuisine, 'ClassesNum': toNumber}


# np.save('train', data_save)

train = np.load('train.npy')

ingredients = list(train[()]['Unqiue ingredients'])

def common_extraction(ingr):
	number = ingredients.index(ingr)
	common = filter(lambda x: ingr in x or x in ingr, ingredients[number:])
	if common:
		ingredients.remove(common)
		return common
	else:
		return None

reduction = {}
for i in ingredients:
	reduction[i]= common_extraction(i)

print reduction 
		