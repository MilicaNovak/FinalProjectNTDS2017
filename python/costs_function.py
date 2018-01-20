import numpy as np
import pandas as pd

from tqdm import tqdm


usefull_columns = ['genres','keywords','popularity']
Movies = pd.read_csv("../Datasets/Transformed.csv",usecols=usefull_columns)

#Constant definition

#Cost added if the first genre is similar between two films
first_genre = 5
#Cost added if the secondary genre is similar between two films
second_genre = 1
#Cost added by similar keyword identical between two films
keyword_cost = 1

def get_genres(film):
    genres = str(film['genres'])
    if genres == 'nan':
        return[]
    else:
        genres = genres.split(",")
    return genres

def get_keywords(film):
    kw = str(film['keywords'])
    if kw == 'nan':
        return[]
    else:
        kw = kw.split(",")
    return kw

"""Define the cost between the film given in index and the others one."""
costs = np.zeros([Movies.shape[0],Movies.shape[0]])

for i in tqdm(range(0,Movies.shape[0])):
    current_film = Movies.iloc[i]
    genres_current = get_genres(current_film)
    kw_current = get_keywords(current_film)
    popularity_current = current_film['popularity']
    
    for j in range(i,Movies.shape[0]):
        cost = 0
        
        b_film = Movies.iloc[j]
        genres_b = get_genres(b_film)
        popularity_b = b_film['popularity']
        #First we only select the first genre to determine the similarity because it's more important that the other genre.
        if len(genres_current) > 0  & len(genres_b) > 0:
            if (genres_current[0] == genres_b[0]):
                cost += first_genre
            
            #This give us the number of similar genres. We pop the first one because we already compare them.
            cost += np.sum(np.in1d(genres_current,genres_b.pop(0),assume_unique='True')) * second_genre
        
        
        kw_b = get_keywords(b_film)
        #This give us the number of similar keywords.
        cost += np.sum(np.in1d(kw_current,kw_b,assume_unique='True')) * keyword_cost
        
        
        #impossible here because we ignore to much popularity
        #cost = (cost * popularity_b/100) / (popularity_current/100)
        costs[i,j] = cost
        costs[j,i] = cost

#Normalize and the remove the one on the diagonal to avoid self-looping.
for i in range(costs.shape[0]):
    costs[i] = costs[i] / np.max(costs[i])
    costs[i,i] = 0

np.savez_compressed("../../Datasets/costs.npz", costs, costs = costs)
