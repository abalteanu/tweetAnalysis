import sentiment_analysis


def main():

    tweetsFileName = "tweets.txt"
    keyFileName = "keywords.txt"

    print(sentiment_analysis.compute_tweets(tweetsFileName, keyFileName))


if __name__ == "__main__":
    main()
