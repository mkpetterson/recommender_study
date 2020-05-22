import logging
import numpy as np
import pandas as pd

from ast import literal_eval



def predicted_rating(df_users, df_movies, user_id, movie_id):
    """
        Gets the user and movie features from the save csv files. 
        If user and/or movie not found, estimate latent features based on neighbors
        
        Inputs:
        df_users: dataframe with stored latent features for users
        df_movies: dataframe with stored latent features for movies
        user_id: int
        movie_id: int
        
        Returns:
        predicted rating: float        
    """
    
    try:
        # Get features from df and turn from string into list
        user = np.array(df_users.loc[user_id, 'features'])
    except:
        user = find_similar_users(user_id)
        
    try:
        item = np.array(df_movies.loc[movie_id, 'features'])
    except:
        item = find_similar_items(movie_id)

        
    if user.shape == item.shape:
        return np.dot(np.array(user), np.array(item))
    else:
        return -1    
    
def find_similar_users(user_id):
    return np.array(-1)
    
def find_similar_items(movie_id):
    return np.array(1)
def find_similar_users(user_id):
    return np.array(-1)
    
def find_similar_items(movie_id):
    return np.array(1)


def out_of_bounds(df):
    """
    1. Fixes predicted ratings that are > 5 or < 1
    2. Order ratings and find movie titles associated with movie id
    
    Returns dataframe

    """
    df.loc[df['rating']<1, 'rating'] = 1
    df.loc[df['rating']>5, 'rating'] = 5
        
    # Sort values and replace rating with title
    df = df.sort_values(by=['user', 'rating'], ascending=[True, False])
                
    return df    
    

def transform(self, requests):
    """
        Predicts the ratings for a given set of requests.

        Parameters
        ----------
        requests : pandas dataframe, shape = (n_ratings, 2)
                  with columns 'user', 'movie'

        Returns
        -------
        dataframe : a pandas dataframe with columns 'user', 'movie', 'rating'
                    column 'rating' containing the predicted rating
    """

    requests['rating'] = np.random.choice(range(1, 5), requests.shape[0])

        # Get predicted ratings
#        requests['rating'] = requests.apply(lambda x: predicted_rating(x['user'], 
#                                                                       x['movie']), axis=1)

        # Fix out of bounds ratings, create movie ranking
#        requests = out_of_bounds(requests)

    return requests