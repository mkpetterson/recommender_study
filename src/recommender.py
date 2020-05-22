import logging
import numpy as np
import pandas as pd

# Spark imports
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS


class MovieRecommender():
    """Template class for a Movie Recommender system."""

    def __init__(self):
        """Constructs a MovieRecommender"""
        self.logger = logging.getLogger('reco-cs')
        self.model = ALS(userCol='user',
                itemCol='movie',
                ratingCol='rating',
                nonnegative=True,
                regParam=0.1,
                rank=10)
        
        self.user_factors_df = pd.read_csv('data/user_factors.csv', index_col='id')
        self.movie_factors_df = pd.read_csv('data/movie_factors.csv', index_col='id')
        

    def fit(self, ratings):
        """
        Trains the recommender on a given set of ratings.

        Parameters
        ----------
        ratings : pandas dataframe, shape = (n_ratings, 4)
                  with columns 'user', 'movie', 'rating', 'timestamp'

        Returns
        -------
        self : object
            Returns self.
        """
        self.logger.debug("starting fit")

        spark = SparkSession.builder.getOrCreate()
        spark_df = spark.createDataFrame(ratings)
        spark_df = spark_df.drop('timestamp')
        
#         # train/validation split
#         train, validation = spark_df.randomSplit([0.8, 0.2])
        self.recommender = self.model.fit(spark_df)

        self.logger.debug("finishing fit")
        return(self)
    
    
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

        return np.dot(np.array(user), np.array(item))


    def find_similar_users(user_id):
        return -1

    def find_similar_items(movie_id):
        return 1

    
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
        self.logger.debug("starting predict")
        self.logger.debug("request count: {}".format(requests.shape[0]))

#         requests['rating'] = np.random.choice(range(1, 5), requests.shape[0])

        # Get predicted ratings
        requests['rating'] = requests.apply(lambda x: predicted_rating(x['user'], 
                                                                       x['movie']), axis=1)


        self.logger.debug("finishing predict")
        return(requests)
        


if __name__ == "__main__":
    logger = logging.getLogger('reco-cs')
    logger.critical('you should use run.py instead')
