# set environment:
import snscrape.modules.twitter as sntwitter
import pandas as pd

# tool parameters, refine tweet search:
query = "RacistEU until:2022-03-25 since:2022-02-27"
limit = 10000

# empty list
tweets = []

# column headers
columns= ['url', 'datetime', 'tweet', 'tweet_id', 'mentioned_user',
          'username', 'display_name', 'user_id', 'if_verified', 'acc_created', 'hashtags', 
          'likeCount', 'quoteCount', 'replyCount', 'retweetCount','retweetedTweet', 'source']

# scrape function
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
  if len(tweets) == limit:
    break
  else:
    tweets.append([tweet.url, tweet.date, tweet.content, tweet.id, tweet.mentionedUsers,
                  tweet.user.username,tweet.user.displayname, tweet.user.id, tweet.user.verified, tweet.user.created, tweet.hashtags,
                  tweet.likeCount, tweet.quoteCount, tweet.replyCount, tweet.retweetCount, tweet.retweetedTweet, tweet.source])

# # tweets dataframe:
df = pd.DataFrame(tweets, columns=columns)

# Store csv data in zip:
df.to_csv('/home/musebe/code/Code4Africa/data/RacistEU_tweets.csv.gz', compression='gzip')