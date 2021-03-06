"""Function File"""

'''CONSTANTS'''
# coordinate constants for region ranges
P1 = (49.189787, -67.444574)
P2 = (24.660845, -67.444574)
P3 = (49.189787, -87.518395)
P4 = (24.660845, -87.518395)
P5 = (49.189787, -101.998892)
P6 = (24.660845, -101.998892)
P7 = (49.189787, -115.236428)
P8 = (24.660845, -115.236428)
P9 = (49.189787, -125.242264)
P10 = (24.660845, -125.242264)

PUNC = '''!()-[]{};:'"\,<>./?@#$%^&*_~\"\''''


def compute_tweets(f_tweets_name, f_key_name):
    """Main function for computing the tweets"""

    end_list = []  # final list to return
    try:
        f_Tweets = open(f_tweets_name, encoding='utf-8', errors='ignore')
        f_Key = open(f_key_name, encoding='utf-8', errors='ignore')
    except IOError:
        # if one of the files does not exist, return an empty list
        return end_list

    '''Organizing info from f_Key'''
    key_list = organizeKeywords(f_Key)  # key_list is a list of tuples containing a keyword followed by its score

    '''Organizing info from f_Tweets'''
    coordinates_list = []  # list of tuples containing coordinates for each tweet
    tweet_list = []  # list of tweets
    # list that will have four elements, each which will count the number of points in a certain region (E, C, M, P)
    count_of_tweets = [0, 0, 0, 0]
    region_score = [0, 0, 0, 0]  # for the average happiness score of each region
    for item in f_Tweets:
        # iterates through each line in the function
        tweet_info_list = item.rstrip("\n").split(" ")  # line to process taken directly from tweets file
        tempCoordinate = (tweet_info_list[0].strip(",[]"), tweet_info_list[1].strip(",[]"))  # makes coordinate tuple

        coordinates_list.append(tempCoordinate)  # makes a list of tuples (list of coordinates)
        temp_tweet = []  # temporary list containing a list of the individual words in the tweet

        for j in range(5, len(tweet_info_list)):
            # populating list by iterating through each item in original list, starting after unnecessary info
            temp_tweet.append(tweet_info_list[j].lstrip(PUNC).rstrip(PUNC).lower())

        tweet_list.append(temp_tweet)  # adds list of words in individual tweet to a list of tweets
    # counting tweets in each region
    for c in coordinates_list:
        tweetLocation(c, count_of_tweets)

    '''Calculating score'''
    count_of_keyword_tweets = calculateTweetScore(tweet_list, key_list, coordinates_list, region_score)

    # calculating the average happiness score for each region
    for i in range(len(region_score)):
        if count_of_keyword_tweets[i] != 0:
            region_score[i] = region_score[i] / count_of_keyword_tweets[i]
    # print(region_score, count_of_keyword_tweets, count_of_tweets)

    east_tuple = (region_score[0], count_of_keyword_tweets[0], count_of_tweets[0])
    central_tuple = (region_score[1], count_of_keyword_tweets[1], count_of_tweets[1])
    mountain_tuple = (region_score[2], count_of_keyword_tweets[2], count_of_tweets[2])
    pacific_tuple = (region_score[3], count_of_keyword_tweets[3], count_of_tweets[3])

    end_list = [east_tuple, central_tuple, mountain_tuple, pacific_tuple]
    return (end_list)


def organizeKeywords(file):
    """Organizing info from fKey"""
    kList = []
    for item in file:
        # iterating through each keyword and its value, creating a list for each pair
        temp = item.split(",")
        for x in range(len(temp)):
            # removing commas and next line key
            temp[x] = temp[x].strip("\n,")
        # creating large list of all words and their values
        kList.append(temp)
    return kList


def calculateTweetScore(sentence_list, keyword_list, coordinates, region_score_list):
    """Function that takes a sentence, finds keywords, and calculates a score based on keywords in sentence"""
    # sentenceList is a list of sentences (which are lists of words) to compute
    # keywordList is a list of tuples containing the keyword to find (0) and the score of that word
    # lists are passed by reference therefore they do not need to be returned

    countKeywordTweets = [0, 0, 0, 0]  # will count the number of keyword tweets in the list.
    countTweets = [0, 0, 0, 0]

    for tweet in range(len(sentence_list)):
        # iterating through tweets
        tweetRegion = tweetLocation(coordinates[tweet], countTweets)  # determining tweet region
        if tweetRegion == 1 or tweetRegion == 2 or tweetRegion == 3 or tweetRegion == 0:
            # ensuring that only tweets within regions are processed
            scoreTemp = 0.0  # will add the score value of each keyword found
            countKeywords = 0  # will count the number of keywords found in the tweet
            for keyword in keyword_list:
                # iterating through each possible keyword in the list to check if it is a tweet
                for word in sentence_list[tweet]:
                    # iterating through words in tweets
                    if keyword[0] == word:
                        keyword[1] = int(keyword[1])
                        scoreTemp = scoreTemp + keyword[1]
                        countKeywords += 1
            if countKeywords != 0:
                # in order to avoid ZeroDivisionError
                scoreTemp = scoreTemp / countKeywords
                # taking average of sentiment value score divided by number of keywords found in tweet
                tweetRegion = tweetLocation(coordinates[tweet], countKeywordTweets)
                # adding happiness scores to each region in order to calculate them later
                if tweetRegion == 0:
                    region_score_list[0] += scoreTemp
                elif tweetRegion == 1:
                    region_score_list[1] += scoreTemp
                elif tweetRegion == 2:
                    region_score_list[2] += scoreTemp
                elif tweetRegion == 3:
                    region_score_list[3] += scoreTemp
    return (countKeywordTweets)


def tweetLocation(stringCoordinates, regionCount):
    """function that determines in which region a set of coordinates is based on constants above, and counts entries
    for each region"""

    coordinates = []

    for item in stringCoordinates:
        coordinates.append(float(item))

    # print(coordinates)
    if P1[0] >= coordinates[0] >= P2[0]:
        # determining if point is within latitude
        if P1[1] >= coordinates[1] > P3[1]:
            # print(coordinates)
            # Eastern Region found
            regionCount[0] += 1
            return 0
        elif P3[1] >= coordinates[1] > P5[1]:
            # Central Region
            regionCount[1] += 1
            return 1
        elif P5[1] >= coordinates[1] > P7[1]:
            # Mountain Region
            regionCount[2] += 1
            return 2
        elif P7[1] >= coordinates[1] > P9[1]:
            # Pacific Region
            regionCount[3] += 1
            return 3
        else:
            return 4
