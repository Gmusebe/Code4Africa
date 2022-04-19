# Tweet Extraction tool
The `snscrape` tool is designed to extract tweets of Twitter users based on Twitter handles, keywords and has advanced features enabling refined searches based on date/time ranges.

# Prerequisites
1. VScode/ Google Colab/ Juputer Notebook
2. Python 3.10.4

The __advantage__ of the tool over the Twitter API is that it is free and has no limit to the number of extracted tweets.

# Install
> Install the `snscrape` package:
```Python
!pip install snscrape
```
> Install the `pandas` package:
```Python
!pip install pandas
```

# Set Environment
Import the required packages on the pythin notebook/script:
```Python
import snscrape.modules.twitter as sntwitter
import pandas as pd
```
# Extract Data
The function to extract the tweets is as follows:
```Python
# tool parameters, refine tweet search:
query = "State criteria of search"
limit = 'limit(int)'

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
```
> Store Data:
```Python
# # tweets dataframe:
df = pd.DataFrame(tweets, columns=columns)

# Store csv data in zip:
df.to_csv('/Code4Africa/data/RacistEU_tweets.csv.gz', compression='gzip')
```
# Search Criteria
> ## 1. To search tweets of a user:
```Python
query = "Raila"
```
> ## 2. To search a keyword:
```Python
query = "#RacismEU"
```
> ## 3. Twitter advanced Search
### Steps
Login [Twitter]() >> Click on the search box >> Type keyword/user of interest >> Press Enter to search

On the __Search filters__ click on the __Advanced search__

Type the `keyword` and the `date range` desires >> Press Enter

Copy the output in the search bar and paste as query:

Results:
```Python
RacistEU until:2022-03-25 since:2022-02-27
```
