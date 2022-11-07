# tweetAnalysis
Program that analyses tweets based on content and location
Analyze each individual tweet to determine a score – a “happiness score” – for the tweet.
The “happiness score” for a single tweet is found by looking for certain keywords (given 
in keyword file) in a tweet and for each keyword found in that tweet totaling their “sentiment values”.
Each key value is an integer from 1 to 10.
The happiness score for the tweet is simply the sum of the “sentiment values” for keywords
found in the tweet divided by the number of keywords found in the tweet, giving an average of the score. 
Each tweet is also assigned to a region, which is calculated in the program as well.
