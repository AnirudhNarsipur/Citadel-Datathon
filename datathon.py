import math
import statistics
import numpy as np
import pandas as pd
import csv
import sys

# df = pd.read_csv('newerfile.csv ', engine = 'python')
#
# df = df.drop('China', axis=1)
# df = df.drop('Latin America', axis=1)
# df = df.drop('Asia Pacific', axis=1)
#
# print(df)

csv.field_size_limit(10000000)

dfmovieWithTags=pd.read_csv('Movie_with_Tags', engine='python', error_bad_lines=False)


dfmovieWithTags['title']=dfmovieWithTags['title'].str.replace(r"\(.*\)","")

dfmovieWithTags['title']=dfmovieWithTags['title'].map(lambda x: x.strip())

dfRevenue = pd.read_csv('grossesbyregion.csv', engine='python')

# dfmovieWithTags.to_csv('dfmovieWithRegex3.csv')
dfRevenue["genres"]=""
dfRevenue["tags"]=""

# dfmovieWithTags=dfmovieWithTags.drop('genres', axis=1)
# dfmovieWithTags=dfmovieWithTags.drop('tags', axis=1)
dfmovieWithTags=dfmovieWithTags.drop('Unnamed: 0', axis=1)

titleList = []
genreList = []
tagList = []

for i in range(58096):
    titleList.append(dfmovieWithTags.at[i, 'title'])
    genreList.append(dfmovieWithTags.at[i, 'genres'])
    tagList.append(dfmovieWithTags.at[i, 'tags'])

hashGenre = {key: value for key, value in zip(titleList, genreList)}
hashTag = {key: value for key, value in zip(titleList, tagList)}

for i in range(17614):
    title2 = dfRevenue.at[i,'title']
    if title2 in titleList:
        dfRevenue.at[i, 'genres'] = hashGenre.get(title2)
        dfRevenue.at[i, 'tags'] = hashTag.get(title2)

dfRevenue.to_csv('newerfile2.csv')
print(dfmovieWithTags)
print(dfRevenue)
# keyList = []
# valueList = []
# for index, row in dfmovieWithTags.iterrows():
#     keyList.append(row['movieId'])
#     valueList.append(row['title'])
#
# hash = {key: value for key, value in zip(keyList, valueList)}

# print(dfmovieWithTags)
#
# dfTags=pd.read_csv('genome-scores.csv', engine='python')

# dfMovieInd=pd.read_csv('movie_industry.csv', engine='python')
#
# dfTags['title'] = ""
#
#
# dfMovieIndList = dfMovieInd["name"].tolist()
#
# dfMovieIndSet = set(dfMovieIndList)


# for i in range(14862528):
#     id = dfTags.at[i,'movieId']
#     # print(i)
#     if id in dfMovieIndSet:
#
#         dfTags.at[i,'title'] = hash.get(id)
#     # else:
#     #
#     #     dfTags.drop(dfTags.index[i])
#
# dfTags.to_csv('newfile.csv')
#
# print(dfTags)


# df = pd.read_csv('newfile.csv', engine='python')
#
# for i in range(0, 10000000, 1100):
#     print(i)
#     print(df.at[i, 'title'])






# dfMovieIndustry = pd.read_csv('movie_industry.csv', engine='python')

# dfMovies=pd.read_csv('movies.csv', engine='python')
#
# dfMovies["tags"]=""
# dfTags = dfTags.drop('timestamp', axis=1)
# dfTags = dfTags.drop('userId', axis=1)
#
# indexList = []
#
# for x in range(58098):
#     dfMovies.at[x,'tags']=[]
#     indexList.append(x)
#
# movieIDList = dfMovies['movieId'].to_list()
#
# hash = {key: value for key, value in zip(movieIDList, indexList)}
# hash = {key: value for key, value in zip(movieIDList, indexList)}
#
# for index, row in dfTags.iterrows():
#     index2 = hash.get(row['movieId'])
#     prev = dfMovies.at[index2, 'tags']
#     prev.append(row['tag'])
#     dfMovies.at[index2, 'tags'] = prev
#
# print(dfMovies)
#
# dfMovies.to_csv('Movie_with_Tags')