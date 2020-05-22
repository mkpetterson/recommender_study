# Recommender Case Study

![badge](https://img.shields.io/badge/last%20modified-may%20%202020-success)
![badge](https://img.shields.io/badge/status-in%20progress-yellow)

<a href="https://github.com/cwong90">Cindy Wong</a> | <a href="https://github.com/rasbot">Nathan Rasmussen</a> | <a href="https://github.com/mkpetterson">Maureen Petterson</a>

## Table of Contents

- <a href="https://github.com/mkpetterson/recommender_study#introduction">Introduction</a>  
- <a href="https://github.com/mkpetterson/recommender_study#data-preparation-and-exploratory-data-analysis">Data Preparation and Exploratory Data Analysis</a> 
- <a href="https://github.com/mkpetterson/recommender_study#modeling-linear-regression">Statistical Analysis</a>  
- <a href="https://github.com/mkpetterson/recommender_study#prediction-results">Prediction Results</a> 
- <a href="https://github.com/mkpetterson/recommender_study#conclusion">Conclusion</a>
- <a href="https://github.com/mkpetterson/recommender_study#notes">Notes</a>


## Introduction

No one wants to waste their time watching movies and tv shows they don't enjoy, but there are so many options for what movies to watch that consumers can struggle to make a decision. 
Companies are eager to pull in users and generate more revenue and relatively newer players such as Netflix and Amazon have started producing their own movies and tv shows. Competition for attention is fierce and more sophisticated technology is leading the way in both giving consumers what they want and in shaping shaping their tastes. Recommender systems are the basis of Netflix, a company that has been wildly successful in amassing a large subscription due to their tailored suggestions and high quality programs (well, compared to reality television).

We have built a movie recommender system based off of 800,000 reviews given by nearly 5400 users. The data comes from the [MovieLens dataset](http://grouplens.org/datasets/movielens/) and it includes movie information, user information, and the users' ratings. 


## Data Preparation and Exploratory Data Analysis

The data did not require any cleaning prior to use, however we did have several different datasets that needed to be linked together to get final recommendations. 

<b>Training Data</b><br>
The training data contained a combined 800,000 reviews. Overall, there were 3662 movies reviewed and 5399 unique users. Most of the users rated over 1000 movies, but the majority rated fewer than 100. A breakdown of the count can be shown in the plot below.


<img src='images/rating_count_by_user.png'>


<b>Movie Data</b>

<b>User Data</b>

<b>Required Predictions</b>
    
    
  
 




- cold starts by count
- ratings given by users
- stats on training and request data
- screenshots of movie and user demographic data


<details>
    <summary>Histogram Showing Cold Starts</summary>
    <img alt="coldstart" src='images/cold_starthist.png'>
</details>
    






<details>
    <summary>Histogram of Features</summary>
<img alt="Histograms" src='img/histograms_of_features.png'>
</details>

<details>
    <summary>Binary Features Bar Chart</summary>
<p align='middle'>
    <td><img src='img/binary_bar_chart.png' align='center' width="400"></td>
</p>
</details>


## Statistical Analysis

We split our training data up into a training and cross validation set in order to tune hyperparameters and pick an optimal error metric for assessing our recommender.

## Prediction Results

## Conclusion


