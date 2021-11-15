import sentiment_analysis


def main():

    tweetsFileName = "tweets1.txt"
    keyFileName = "key1.txt"

    print(sentiment_analysis.compute_tweets(tweetsFileName, keyFileName))


if __name__ == "__main__":
    main()
