#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 16:04:47 2020

@author: Danial
"""
import pandas as pd
import numpy as np
import pickle

# read in foreign IDs and mappings
foreignId = pickle.load(open("foreign_movie_ids.pkl", "rb"))

user2user_encoded = pickle.load(open("user2newUser_map", "rb"))
movie2movie_encoded = pickle.load(open("movie2newmovie_map", "rb"))
movie_encoded2movie = pickle.load(open("newMovie2movie_map", "rb"))

newForeignId = [movie2movie_encoded[i] for i in foreignId if i in movie2movie_encoded]

# read in learned embeddings from Jl
movie_embedding_learnt = np.load('movie_embedding_learnt.npy')
user_embedding_learnt = np.load('user_embedding_learnt.npy')

def recommend(user_id, number_of_movies=5):
    newuserId = user2user_encoded[user_id]
    movies = user_embedding_learnt[newuserId]@movie_embedding_learnt.T
    movies[[i for i in range(len(movies)) if i not in newForeignId]] = np.NINF
    mids = np.argpartition(movies, -number_of_movies)[-number_of_movies:]
    return [movie_encoded2movie[i] for i in mids]

# e.g. read in set of "englishUsers" (viewers who only reviewed english language movies),
# pick one at random, and generate best foreign movie recommendations 
    
englishUsers = list(pickle.load(open("english_users_sub.pkl", "rb")))

user = englishUsers[42]
print(recommend(user)) # foreign recs for userId 2182 who never reviewed any foreign movies
                       # we can look up the foreign movieIds to manually validate our results


