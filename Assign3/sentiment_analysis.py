'''Function File'''

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


def compute_tweets(f_tweets_name, f_key_name):
    endList = []  # final list to return
    try:
        fTweets = open(f_tweets_name, encoding='utf-8', errors='ignore')
        fKey = open(f_key_name, encoding='utf-8', errors='ignore')
    except IOError:
        # if one of the files does not exist, return an empty list
        return endList


    '''Organizing info from fKey'''
    keyList = organizeKeywords(fKey) #keyList is a list of touples containing a keyword followed by its score

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
            tempTweet.append(tweetInfoL[j].lstrip(".#?!-_\n").rstrip(".#?!-_\n").lower())
        # adds list of words in individual tweet to a list of tweets
        tweetList.append(tempTweet)

    # list that will have four elements, each which will count the number of points in a certain region (E, C, M, P)
    regionTweetCount = [0, 0, 0, 0]
    # counting tweets in each region
    for c in coordinatesList:
        tweetLocation(c, regionTweetCount)
    print(regionTweetCount)


    '''Calculating score'''
    scoreList = []
    regionKeywordTweetCount = calculateTweetScore(scoreList, tweetList, keyList, coordinatesList)


    # For now, the function returns a list of scores.
    return(scoreList)


'''Organizing info from fKey'''
def organizeKeywords(file):

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

def calculateTweetScore(score, sentenceList, keywordList, coordinates):
    '''Function that takes a sentence, finds keywords, and calculates a score based on keywords in sentence'''
    # score is an ordered list of the happiness score value of each tweet
    # sentenceList is a list of sentences (which are lists of words) to compute
    # keywordList is a list of tuples containing the keyword to find (0) and the score of that word
    # lists are passed by reference therefore they do not need to be returned
    countKeywordTweets = [0,0,0,0] # will count the number of keyword tweets in the list.

    for tweet in range(len(sentenceList)):

        #print("Tweet: ", tweet)
        # iterating through tweets
        scoreTemp=0.0   # will add the score value of each keyword found
        countKeywords=0 # will count the number of keywords found in the tweet

        for keyword in keywordList:
            # iterating through each possible keyword in the list to check if it is a tweet
            #print("Keyword: ", keyword)
            for word in sentenceList[tweet]:
                #print("Word in tweet: ", word)
                # iterating through words in tweets
                if keyword[0] == word:
                    keyword[1] = int(keyword[1])
                    scoreTemp = scoreTemp + keyword[1]
                    #print(keyword[1], scoreTemp)
                    countKeywords+=1


        # taking average of sentiment value score divided by number of keywords found in tweet
        if countKeywords == 0:
            # in order to avoid ZeroDivisionError
            score.append(0)
        else:
            tweetLocation(coordinates[tweet], countKeywordTweets)

            scoreTemp = scoreTemp/countKeywords
            score.append(scoreTemp)
    #print(countKeywordTweets)
    return(countKeywordTweets)

def tweetLocation(stringCoordinates, regionCount):
    '''function that determines in which region a set of coordinates is based on constants above'''

    coordinates = []
    for item in stringCoordinates:
        coordinates.append(float(item))

    #print(coordinates)
    if coordinates[0] < P1[0] and coordinates[0] > P2[0]:
        # determining if point is within latitude
        if coordinates[1] < P1[1] and coordinates[1] > P3[1]:
            # Eastern Region found
            regionCount[0] += 1
        elif coordinates[1] < P3[1] and coordinates[1] > P5[1]:
            # Central Region
            regionCount[1] += 1
        elif coordinates[1] < P5[1] and coordinates[1] > P7[1]:
            # Mountain Region
            regionCount[2] += 1
        elif coordinates[1] < P7[1] and coordinates[1] > P9[1]:
            # Pacific Region
            regionCount[3] += 1
