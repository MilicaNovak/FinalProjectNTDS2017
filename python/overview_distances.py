#For text mining
from stemming.porter2 import stem
from tqdm import tqdm
import math
import collections
import scipy
import pandas as pd
import numpy as np


def get_film_words(film):
    stop_words = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']
    
    overview = str(film['overview'])
    if overview == 'nan':
        return collections.Counter([])
    
    words = [i for i in film['overview'].lower().split() if i not in stop_words]

    for word in words:
        word = stem(word)
    
    return collections.Counter(words)

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

Movies = pd.read_csv("../Datasets/Transformed.csv")
cosine_distances = np.zeros([Movies.shape[0],Movies.shape[0]])
    
for m in tqdm(range(Movies.shape[0])):
    current_words = get_film_words(Movies.iloc[m])
        
    for n in range(m, Movies.shape[0]):
            
        words = get_film_words(Movies.iloc[n])
        cosine = get_cosine(current_words,words)
            
        cosine_distances[m,n] = cosine
        cosine_distances[n,m] = cosine

np.savez_compressed("../../Datasets/cosine_compressed.npz", cosine_distances, cosine = cosine_distances)
