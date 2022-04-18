import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "RacistEU until:2022-03-25 since:2022-02-27"
tweets = []
limit = 10000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
  
  # print(vars(tweet))
  # break
  if len(tweets) == limit:
    break
  else:
    tweets.append([tweet.date,tweet.username,tweet.id, tweet.content, tweet.url, tweet.hashtags, tweet.likeCount, tweet.quoteCount, tweet.replyCount, tweet.retweetCount, tweet.retweetedTweet, tweet.sourceUrl ])

df = pd.DataFrame(tweets)

# Store Data in csv:
df.to_csv('/home/musebe/code/Code4Africa/data/RacistEU_tweets.csv')

# Json then zip....