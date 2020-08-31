import pandas as pd
import GetOldTweets3 as got
import csv

username="MOH_Kenya"
text_query="COVID-19 UPDATE"
start="2020-04-01"
stop="2020-08-01"
count=1000

#creation of query object
tweetCriteria = got.manager.TweetCriteria().setUsername(username).setQuerySearch(text_query).setSince(start).setUntil(stop).setMaxTweets(count)
#Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
#Creating a list of the choosen tweets above
user_tweets = [[tweet.date, tweet.text, tweet.retweets] for tweet in tweets]
#Creation of a dataframe for the list formed
tweets_df = pd.DataFrame(user_tweets)
#Writing and creating a csv file for the dataframe
tweets_df.to_csv(r'mohtweets4.csv' , header=True)
#tweets_df.shape
#print(tweets_df)

