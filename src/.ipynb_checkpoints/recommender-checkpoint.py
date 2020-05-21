import logging
import numpy as np
import pandas as pd

# Spark imports
from pyspark.sql import SparkSession


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
        try:
            user = self.recommender.userFactors.where(f'id == {user_id}').collect()[0]['features']
        except:
            user = find_similar_users(user_id)
            
        try:
            item = self.recommender.itemFactors.where(f'id == {movie_id}').collect()[0]['features']
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

        for user, movie in requests:

        self.logger.debug("finishing predict")
        return(requests)
        


if __name__ == "__main__":
    logger = logging.getLogger('reco-cs')
    logger.critical('you should use run.py instead')
