import math
import statistics
import numpy as np
import pandas as pd

dfTags=pd.read_csv('tags.csv', engine='python')

dfMovies=pd.read_csv('movies.csv', engine='python')

dfMovies["tags"]=""
dfTags = dfTags.drop('timestamp', axis=1)
dfTags = dfTags.drop('userId', axis=1)

indexList = []

for x in range(58098):
    dfMovies.at[x,'tags']=[]
    indexList.append(x)

movieIDList = dfMovies['movieId'].to_list()

hash = {key: value for key, value in zip(movieIDList, indexList)}

for index, row in dfTags.iterrows():
    index2 = hash.get(row['movieId'])
    prev = dfMovies.at[index2, 'tags']
    prev.append(row['tag'])
    dfMovies.at[index2, 'tags'] = prev

print(dfMovies)
