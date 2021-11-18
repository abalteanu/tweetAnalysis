# Ana Balteanu
# Computer Science 1026
# Professor Bryan Sarlo
# November 17, 2021


'''Assignment 3 - Sentiment Analysis Program'''
# This program analyses tweets based on keywords and keyword values, as well as the location of the tweet in order to
# determine an overall happiness score in each area: Eastern, Central, Mountain, Pacific. In this program, a series of
# functions determine the region of each tweet, separate different aspects of the keyword and tweets file, and determine
# the average happiness score.
# The program outputs the average happiness scrore, the tweets, and the tweets containing keywords for each region.


import sentiment_analysis

def main():

    # asking user for input
    key_file_name = input("Enter keyword file name: ")
    tweets_file_name = input("Please enter the tweets file: ")

    tweet_analysis = sentiment_analysis.compute_tweets(tweets_file_name, key_file_name)

    '''OUTPUT'''
    if not tweet_analysis:
        # if compute_tweets goes through try/except statement and cannot open file, it returns an empty list
        print("Error: empty list returned")
    else:
        print("\nEASTERN")
        print("Average happiness score: %.2f" % round(tweet_analysis[0][0], 2))
        print("Tweets in this region containing a keyword: %.2f" % round(tweet_analysis[0][1], 2))
        print("Number of tweets in this region: %.2f"% round(tweet_analysis[0][2], 2))


        print("\nCENTRAL")
        print("Average happiness score: %.2f" % round(tweet_analysis[1][0], 2))
        print("Tweets in this region a keyword: %.2f" % round(tweet_analysis[1][1], 2))
        print("Number of tweets in this region: %.2f"% round(tweet_analysis[1][2], 2))

        print("\nMOUNTAIN")
        print("Average happiness score: %.2f" % round(tweet_analysis[2][0], 2))
        print("Tweets in this region a keyword: %.2f" % round(tweet_analysis[2][1], 2))
        print("Number of tweets in this region: %.2f"% round(tweet_analysis[2][2], 2))



        print("\nPACIFIC")
        print("Average happiness score: %.2f" % round(tweet_analysis[3][0], 2))
        print("Tweets in this region a keyword: %.2f" % round(tweet_analysis[3][1], 2))
        print("Number of tweets in this region: %.2f"% round(tweet_analysis[3][2], 2))




if __name__ == "__main__":
    main()
