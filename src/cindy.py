from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

user_factors_df = pd.read_csv('data/user_factors_all.csv', index_col='id')
movie_factors_df = pd.read_csv('data/movie_factors_all.csv', index_col='id')
movies_sim_mat = pd.read_csv('data/movies_sim_mat.csv', index_col='movie_id')
users_sim_mat = pd.read_csv('data/users_sim_mat.csv', index_col='user_id')


def predicted_rating(user_id, movie_id):
    """
    Gets the user and movie features from the save csv files. 
    If user and/or movie not found, estimate latent features based on neighbors
    
    Inputs:
    user_id: int
    movie_id: int
    
    Returns:
    predicted rating: float        
    """
    
    try:
        # Get features from df and turn from string into list
        u_features = literal_eval(self.user_factors_df.loc[user_id, 'features'])
        user = np.array(u_features)
    except:
        user = find_similar_users(user_id)
    try:
        i_features = literal_eval(self.movie_factors_df.loc[movie_id, 'features'])
        item = np.array(i_features)
    except:
        item = find_similar_items(movie_id)
    # Check if they are same shape
    if user.shape == item.shape:
        return np.dot(np.array(user), np.array(item))
    else:
        return

                                  
# CODE TO RECREATE MOVIES/USERS SIMILARITY MATRIX, NOT NECESSARY ONCE DOWNLOADED CSV
def movies_sim_matrix(movies_df):
    """
    Create cosine similarity matrix for movies using a DataFrame containing movies information.
    Item-item similarity. Read in movies.csv file.
    
    Inputs:
    movies_df: pandas DataFrame
    
    Outputs:
    movies_sim_mat: pandas DataFrame
    """
    movies_df.set_index('movie_id', inplace=True)
                                  
    tf = TfidfVectorizer()
    movies_tfidf = tf.fit_transform(movies_df['genre'])
    movies_indices = pd.Series(movies_df.index)
    movies_sim_mat = pd.DataFrame(cosine_similarity(movies_tfidf), index=movies_indices,
                                  columns=movies_indices)
    movies_sim_mat.to_csv('data/movies_sim_mat.csv')
    return 'movies_sim_mat.csv saved.'
    

def users_sim_matrix(users_demo_df):
    """
    Create cosine similarity matrix for users using a DataFrame containing user demographic information.
    User-user similarity. Read in users.csv file.
    
    Inputs:
    users_demo_df: pandas DataFrame
    
    Outputs:
    users_sim_mat: pandas DataFrame
    """
    users_demo_df.set_index('user_id', inplace=True)
                                  
    users_indices = pd.Series(users_demo_df.index)
    users_sim_mat = pd.DataFrame(cosine_similarity(users_demo_df), index=users_indices,
                                 columns=users_indices)
    users_sim_mat.to_csv('data/users_sim_mat.csv')
    return 'users_sim_mat.csv saved.'
                                  
                                  
# FINDING SIMILIARTY CODE TO ADD TO RECOMMENDER.PY
def find_similar_users(user_id):
    """
    Finds similar users and returns best guess for cosine similarity matrix
    
    Inputs:
    user_id: int
            
    """
    if len(user_factors_df.colums) == 2:
        user_factors_df.drop('Unnamed: 0', axis=1)
    
    similar_user_ids = users_sim_mat.loc[users_sim_mat[f'{user_id}'] >= 1, f'{user_id}'][1:].index.values
    
    users = []
    
    for i in similar_user_ids:
        try:
            u_features = user_factors_df.loc[i, 'features']
            user = np.array(u_features)
            users.append(user)
        except:
            continue

    return np.mean(users, axis=0)    


def find_similar_items(movie_id):
    """
    Find similar movies and returns best guess for cosine similarity matrix
    
    Inputs:
    movie_id: int
    
    """
    similar_movie_ids = movies_sim_mat.loc[movies_sim_mat[f'{movie_id}'] >= 1, f'{movie_id}'][1:].index.values
    
    items = []

    for i in similar_movie_ids:
        i_features = movie_factors_df.loc[i, 'features']
        item = np.array(i_features)
        items.append(item)

    return np.mean(items, axis=0)