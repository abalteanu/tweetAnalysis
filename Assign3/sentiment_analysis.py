'''Function File'''


def compute_tweets(f_tweets_name, f_key_name):
    endList = []  # final list to return
    try:
        fTweets = open(f_tweets_name, "r")
        fKey = open(f_key_name, "r")
    except IOError:
        # if one of the files does not exist, return an empty list
        return endList


    '''Organizing info from fKey'''
    keyList = [] #keyList is a list of touples containing a keyword followed by its score

    for item in fKey:
        # iterating through each keyword and its value, creating a list for each pair
        temp = item.split(",")
        for x in range(len(temp)):
            # removing commas and next line key
            temp[x] = temp[x].strip("\n,")
        # creating large list of all words and their values
        keyList.append(temp)


    '''Organizing info from fTweets'''
    coordinatesList = []
    tweetList = []

    for item in fTweets:
        # iterates through each line in the function
        tweetInfoL = item.split(" ")
        tempCoordinate = (tweetInfoL[0].strip(",[]"), tweetInfoL[1].strip(",[]"))  # makes coordinate tuple
        coordinatesList.append(tempCoordinate)  # makes a list of tuples (list of coordinates)
        tempTweet = []  # temporary list containing a list of the individual words in the tweet

        for j in range(5, len(tweetInfoL)):
            # populating list by iterating through each item in original list, starting after unnecessary info
            tempTweet.append(tweetInfoL[j].lstrip(".#?!-_\n").rstrip(".#?!-_\n"))
        # adds list of words in individual tweet to a list of tweets
        tweetList.append(tempTweet)

        # print(coordinatesList)
        # print(tweetList)
        # print(item)


    '''Calculating score'''
    # score is an ordered list of the happiness score value of each tweet
    score = []
    for tweet in range(len(tweetList)):

        print("Tweet: ", tweet)
        # iterating through tweets
        scoreTemp=0.0   # will add the score value of each keyword found
        countKeywords=0 # will count the number of keywords found in the tweet

        for keyword in keyList:
            # iterating through each possible keyword in the list to check if it is a tweet
            print("Keyword: ", keyword)
            for word in tweetList[tweet]:
                print("Word in tweet: ", word)
                # iterating through words in tweets
                if keyword[0] == word:
                    keyword[1] = int(keyword[1])
                    scoreTemp = scoreTemp + keyword[1]
                    print(keyword[1], scoreTemp)
                    countKeywords+=1


        # taking average of sentiment value score divided by number of keywords found in tweet
        if countKeywords == 0:
            # in order to avoid ZeroDivisionError
            score.append(0)
        else:
            scoreTemp = scoreTemp/countKeywords
            score.append(scoreTemp)
    print(tweetList[0], score[0])
    print(tweetList[1], score[1])




    # For now, the function returns a list of scores.
    return(score)
