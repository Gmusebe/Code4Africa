<p align="center">
  <img src="https://avatars.githubusercontent.com/u/2786364?s=200&v=4" alt="Sublime's custom image"/>
</p>

# [Code for Africa](https://opportunities.codeforafrica.org/)
Code for Africa (CfA) is the continent’s largest network of civic technology and data journalism labs, with teams in 21 countries. CfA builds digital democracy solutions that give citizens unfettered access to actionable information that empowers them to make informed decisions, and that strengthens civic engagement for improved public governance and accountability.
# Analysis
[Code for Africa]((https://opportunities.codeforafrica.org/)) case study.

# Repository structure

* [Setting Environment](https://github.com/Gmusebe/Code4Africa#setting-environment)
* [Data Collection](https://github.com/Gmusebe/Code4Africa#data-collection)
* [Copyright and license](https://github.com/Gmusebe/Code4Africa#copyright-and-license)


## Setting Environment
The packages required for development of our tools are set by importing them as follows:
```Python
import re
import collections
import pandas as pd
import cufflinks as cf
import plotly.offline as py
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

from nltk.tokenize import WordPunctTokenizer

token = WordPunctTokenizer()

cf.go_offline() # required to use plotly offline
py.init_notebook_mode() # graphs charts inline (IPython).
```
> Should you be new in using python/or are working on a new virtual environment, the following libraries may not be available and can be installed through `pip` or `conda`. This is likewise on [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb) having the basic packages already installed
```Python
> pip install package_name
```
# Data Collection
Utilize the `snscrape` twitter data extraction tool to scrape tweets by __username(s)__, __keywords__, and in advanced searcahes __timelimits__. 
```Python
query = "State criteria of search"
tweets = [] # Empty list 
limit = 'limit(int)' # least number of tweets returned

# column headers
columns= ['url', 'datetime', 'tweet', 'tweet_id', 'mentioned_user', 'user',
          'username', 'display_name', 'user_id', 'if_verified', 'acc_created', 'hashtags', 
          'likeCount', 'quoteCount', 'replyCount', 'retweetCount','retweetedTweet', 'source']

# scrape function
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
  if len(tweets) == limit:
    break
  else:
    tweets.append([tweet.url, tweet.date, tweet.content, tweet.id, tweet.mentionedUsers, tweet.user,
                  tweet.user.username,tweet.user.displayname, tweet.user.id, tweet.user.verified, tweet.user.created, tweet.hashtags,
                  tweet.likeCount, tweet.quoteCount, tweet.replyCount, tweet.retweetCount, tweet.retweetedTweet, tweet.source])

# # tweets dataframe:
df = pd.DataFrame(tweets, columns=columns)

# Store csv data in zip:
df.to_csv('/home/musebe/code/Code4Africa/data/RacistEU_tweets.csv.gz', compression='gzip')
```
> The above tool has two major parameters:
* __query__ :defines the search critea; whether a username, keyword/hashtags and date limits.
* __limit__ : defines the maximum amount of tweets to be extracted (if more is available).

Saving our data into a desired local file, the tool provides us with such kind of data:


|  | datetime | user | username | tweet_id | tweet | tweet_url | hashtags | likeCount | quoteCount | replyCount | retweetCount | retweetedTweet | sourceUrl |
|- | -------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2022-03-24 10:32:23+00:00 | https://twitter.com/ScorpionPlan | ScorpionPlan | 1506941991954910000 | @irvinmigue @FicoGutierrez #Racista #racistas #racist #racisteu | https://twitter.com/ScorpionPlan/status/1506941991954919425 | ['Racista', 'racistas', 'racist', 'racisteu'] | 0 | 0 | 1 | 0 |  | http://twitter.com/download/android |
| 1 | 2022-03-24 09:52:22+00:00 | https://twitter.com/SilenceIsGolddd | SilenceIsGolddd | 1506931921087040000| #RacistEU #RacistUkraine #NoMoreUSHypocrisy #No2TheWest #NewWorldOrder https://t.co/7nwOSyMGEt | https://twitter.com/SilenceIsGolddd/status/1506931921087049734 | ['RacistEU', 'RacistUkraine', 'NoMoreUSHypocrisy', 'No2TheWest', 'NewWorldOrder'] | 2 | 1 | 0 | 1 | --- | http://twitter.com/download/android |
| 2 | 2022-03-23 22:48:15+00:00 | https://twitter.com/segenmsemere | segenmsemere | 1506764790341020000 | #AfricanRefugees #racisteu https://t.co/lHVlMTqW6x | https://twitter.com/segenmsemere/status/1506764790341029897 | ['AfricanRefugees', 'racisteu'] | 0 | 0 | 0 | 0 | --- | http://twitter.com/download/iphone |
| 3 | 2022-03-23 17:57:28+00:00 | https://twitter.com/blindninja2 | blindninja2 | 1506691612298160000 | The sanctions toward Russia are backfiring. The rest of the world that is people of color.The US really screwed up #AfricansinUkraine #BlackLivesMatter #racisteu #gasprices #Ukraine https://t.co/WinKMexR51 | https://twitter.com/blindninja2/status/1506691612298162179 | ['AfricansinUkraine', 'BlackLivesMatter', 'racisteu', 'gasprices', 'Ukraine'] | 1 | 0 | 1 | 0 |  | http://twitter.com/download/iphone |


[_Click here_](https://github.com/Gmusebe/Code4Africa/tree/master/tool) To learn more about the tool. 

# Copyright and license
The tool has been modified from the  [JustAnotherArchivist](https://github.com/JustAnotherArchivist/snscrape) repo.
