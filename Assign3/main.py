import sentiment_analysis


def main():

    tweetsFileName = "tweets_Ana.txt"
    keyFileName = "keywords_Ana.txt"

    print(sentiment_analysis.compute_tweets(tweetsFileName, keyFileName))


if __name__ == "__main__":
    main()
