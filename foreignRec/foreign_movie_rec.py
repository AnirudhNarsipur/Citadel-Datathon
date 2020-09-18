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
foreignId = pickle.load(open("'foreign_movie_ids.pkl'", "rb"))

user2user_encoded = pickle.load(open("user2newUser_map", "rb"))
movie2movie_encoded = pickle.load(open("movie2newmovie_map", "rb"))
movie_encoded2movie = pickle.load(open("newMovie2movie_map", "rb"))

newForeignID = [movie2movie_encoded[i] for i in foreignId]

# read in learned embeddings from Jl
movie_embedding_learnt = np.load('movie_embedding_learnt.npy')
user_embedding_learnt = np.load('user_embedding_learnt.npy')

def recommend(user_id, number_of_movies=5):
    newuserId = user2user_encoded[user_id]
    movies = user_embedding_learnt[newuserId]@movie_embedding_learnt.T
    movies[~newForeignId] = np.NINF
    mids = np.argpartition(movies, -number_of_movies)[-number_of_movies:]
    return [movie_encoded2movie[i] for i in mids]
