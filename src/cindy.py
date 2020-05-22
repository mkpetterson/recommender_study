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
        user = find_similar_users(user_
    try:
        i_features = literal_eval(self.movie_factors_df.loc[movie_id, 'features'])
        item = np.array(i_features)
    except:
        item = find_similar_items(movie_
    # Check if they are same shape
    if user.shape == item.shape:
        return np.dot(np.array(user), np.array(item))
    else:
        return
                                  
def find_similar_users(user_id):
    """
    Finds similar users and returns best guess for laten features matrix
            
    """
    return np.array(
def find_similar_items(movie_id):
    """
    Find similar movies and returns best guess for latent features matrix
    
    """
    return np.array(1)