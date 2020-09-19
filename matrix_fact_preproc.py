#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:56:05 2020

@author: Danial
"""

iso_639_choices = dict([('ab', 'Abkhaz'),
('aa', 'Afar'),
('af', 'Afrikaans'),
('ak', 'Akan'),
('sq', 'Albanian'),
('am', 'Amharic'),
('ar', 'Arabic'),
('an', 'Aragonese'),
('hy', 'Armenian'),
('as', 'Assamese'),
('av', 'Avaric'),
('ae', 'Avestan'),
('ay', 'Aymara'),
('az', 'Azerbaijani'),
('bm', 'Bambara'),
('ba', 'Bashkir'),
('eu', 'Basque'),
('be', 'Belarusian'),
('bn', 'Bengali'),
('bh', 'Bihari'),
('bi', 'Bislama'),
('bs', 'Bosnian'),
('br', 'Breton'),
('bg', 'Bulgarian'),
('my', 'Burmese'),
('ca', 'Catalan; Valencian'),
('ch', 'Chamorro'),
('ce', 'Chechen'),
('ny', 'Chichewa; Chewa; Nyanja'),
('zh', 'Chinese'),
('cv', 'Chuvash'),
('kw', 'Cornish'),
('co', 'Corsican'),
('cr', 'Cree'),
('hr', 'Croatian'),
('cs', 'Czech'),
('da', 'Danish'),
('dv', 'Divehi; Maldivian;'),
('nl', 'Dutch'),
('dz', 'Dzongkha'),
('en', 'English'),
('eo', 'Esperanto'),
('et', 'Estonian'),
('ee', 'Ewe'),
('fo', 'Faroese'),
('fj', 'Fijian'),
('fi', 'Finnish'),
('fr', 'French'),
('ff', 'Fula'),
('gl', 'Galician'),
('ka', 'Georgian'),
('de', 'German'),
('el', 'Greek, Modern'),
('gn', 'Guaraní'),
('gu', 'Gujarati'),
('ht', 'Haitian'),
('ha', 'Hausa'),
('he', 'Hebrew (modern)'),
('hz', 'Herero'),
('hi', 'Hindi'),
('ho', 'Hiri Motu'),
('hu', 'Hungarian'),
('ia', 'Interlingua'),
('id', 'Indonesian'),
('ie', 'Interlingue'),
('ga', 'Irish'),
('ig', 'Igbo'),
('ik', 'Inupiaq'),
('io', 'Ido'),
('is', 'Icelandic'),
('it', 'Italian'),
('iu', 'Inuktitut'),
('ja', 'Japanese'),
('jv', 'Javanese'),
('kl', 'Kalaallisut'),
('kn', 'Kannada'),
('kr', 'Kanuri'),
('ks', 'Kashmiri'),
('kk', 'Kazakh'),
('km', 'Khmer'),
('ki', 'Kikuyu, Gikuyu'),
('rw', 'Kinyarwanda'),
('ky', 'Kirghiz, Kyrgyz'),
('kv', 'Komi'),
('kg', 'Kongo'),
('ko', 'Korean'),
('ku', 'Kurdish'),
('kj', 'Kwanyama, Kuanyama'),
('la', 'Latin'),
('lb', 'Luxembourgish'),
('lg', 'Luganda'),
('li', 'Limburgish'),
('ln', 'Lingala'),
('lo', 'Lao'),
('lt', 'Lithuanian'),
('lu', 'Luba-Katanga'),
('lv', 'Latvian'),
('gv', 'Manx'),
('mk', 'Macedonian'),
('mg', 'Malagasy'),
('ms', 'Malay'),
('ml', 'Malayalam'),
('mt', 'Maltese'),
('mi', 'Māori'),
('mr', 'Marathi (Marāṭhī)'),
('mh', 'Marshallese'),
('mn', 'Mongolian'),
('na', 'Nauru'),
('nv', 'Navajo, Navaho'),
('nb', 'Norwegian Bokmål'),
('nd', 'North Ndebele'),
('ne', 'Nepali'),
('ng', 'Ndonga'),
('nn', 'Norwegian Nynorsk'),
('no', 'Norwegian'),
('ii', 'Nuosu'),
('nr', 'South Ndebele'),
('oc', 'Occitan'),
('oj', 'Ojibwe, Ojibwa'),
('cu', 'Old Church Slavonic'),
('om', 'Oromo'),
('or', 'Oriya'),
('os', 'Ossetian, Ossetic'),
('pa', 'Panjabi, Punjabi'),
('pi', 'Pāli'),
('fa', 'Persian'),
('pl', 'Polish'),
('ps', 'Pashto, Pushto'),
('pt', 'Portuguese'),
('qu', 'Quechua'),
('rm', 'Romansh'),
('rn', 'Kirundi'),
('ro', 'Romanian, Moldavan'),
('ru', 'Russian'),
('sa', 'Sanskrit (Saṁskṛta)'),
('sc', 'Sardinian'),
('sd', 'Sindhi'),
('se', 'Northern Sami'),
('sm', 'Samoan'),
('sg', 'Sango'),
('sr', 'Serbian'),
('gd', 'Scottish Gaelic'),
('sn', 'Shona'),
('si', 'Sinhala, Sinhalese'),
('sk', 'Slovak'),
('sl', 'Slovene'),
('so', 'Somali'),
('st', 'Southern Sotho'),
('es', 'Spanish'),
('su', 'Sundanese'),
('sw', 'Swahili'),
('ss', 'Swati'),
('sv', 'Swedish'),
('ta', 'Tamil'),
('te', 'Telugu'),
('tg', 'Tajik'),
('th', 'Thai'),
('ti', 'Tigrinya'),
('bo', 'Tibetan'),
('tk', 'Turkmen'),
('tl', 'Tagalog'),
('tn', 'Tswana'),
('to', 'Tonga'),
('tr', 'Turkish'),
('ts', 'Tsonga'),
('tt', 'Tatar'),
('tw', 'Twi'),
('ty', 'Tahitian'),
('ug', 'Uighur, Uyghur'),
('uk', 'Ukrainian'),
('ur', 'Urdu'),
('uz', 'Uzbek'),
('ve', 'Venda'),
('vi', 'Vietnamese'),
('vo', 'Volapük'),
('wa', 'Walloon'),
('cy', 'Welsh'),
('wo', 'Wolof'),
('fy', 'Western Frisian'),
('xh', 'Xhosa'),
('yi', 'Yiddish'),
('yo', 'Yoruba'),
('za', 'Zhuang, Chuang'),
('zu', 'Zulu'),])

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

ratings = pd.read_csv('movie_lense/ratings.csv')
movies = pd.read_csv('movie_lense/links.csv')
lang = pd.read_pickle('movie_lense/lang_dict.pkl')

ratings.head()
movies.head()

lang = {k: lang[k] for k in lang if not np.isnan(k)}
movies['og_lang'] = movies['tmdbId'].map(lang)

movies.og_lang.unique()
movies = movies[~movies.og_lang.isin([''])]
movies = movies[~movies.og_lang.isnull()]

topTen = movies.og_lang.value_counts()[:10]

sns.set_style('darkgrid')
plot = sns.barplot(topTen.index.map(iso_639_choices), topTen)
plot.set_xticklabels(plot.get_xticklabels(), rotation=45)
plt.xlabel('original language', fontsize = 14)
plt.ylabel('count', fontsize = 14)
plt.tick_params(labelsize = 12)

def foreignInd(lang):
  if lang == 'en':
    return 0
  else:
    return 1

movies['foreign'] = movies['og_lang'].apply(foreignInd)

# get movie IDs for all foreign films
foreignId = movies.loc[movies.foreign == 1, 'movieId']

# from ratings, find users who have never rated foreign films
foreignUsers = set(ratings.loc[ratings.movieId.isin(foreignId), 'userId'])
englishUsers = set(ratings.userId).difference(foreignUsers)

# filter ratings matrix by users who have never seen foreign movies OR foreign movies
ratingsSub = ratings[(ratings.userId.isin(englishUsers)) | (ratings.movieId.isin(foreignId))]

# filter down ratingsSub keeping proportion of foreign vs english
def foreign_rating(movieId):
    return movieId in foreignId.values

ratingsSub['foreign_review'] = ratingsSub.movieId.apply(foreign_rating)
foreign_ratings = ratingsSub[ratingsSub.foreign_review == True]
eng_ratings = ratingsSub[~ratingsSub.foreign_review == True]

foreign_sub = foreign_ratings.sample(frac = 0.15)
eng_sub = eng_ratings.sample(frac = 0.15)

df = pd.concat([foreign_sub, eng_sub])

# create new indices
user_ids = df["userId"].unique().tolist()
user2user_encoded = {x: i for i, x in enumerate(user_ids)}
userencoded2user = {i: x for i, x in enumerate(user_ids)}

movie_ids = df["movieId"].unique().tolist()
movie2movie_encoded = {x: i for i, x in enumerate(movie_ids)}
movie_encoded2movie = {i: x for i, x in enumerate(movie_ids)}

df["newuserId"] = df["userId"].map(user2user_encoded)
df["newmovieId"] = df["movieId"].map(movie2movie_encoded)

df.to_csv("ratings_for_training.csv")
pickle.dump(foreignId, open('foreign_movie_ids.pkl', 'wb'))
pickle.dump(englishUsers, open('english_users.pkl', 'wb'))

pickle.dump(user2user_encoded, open('user2newUser_map', 'wb'))
pickle.dump(userencoded2user, open('newUser2user_map', 'wb'))
pickle.dump(movie2movie_encoded , open('movie2newMovie_map', 'wb'))
pickle.dump(movie_encoded2movie, open('newMovie2movie_map', 'wb'))
