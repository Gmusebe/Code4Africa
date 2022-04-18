# Tweet Extraction tool
The `snscrape` tool is designed to extract tweets of Twitter users based on Twitter handles, keywords and has advanced features enabling refined searches based on date/time ranges.

# Prerequisites
1. VScode/ Google Colab/ Juputer Notebook
2. Python 3.10.4

The __advantage__ of the tool over the Twitter API is that it is free and has no limit to the number of extracted tweets.

# Install
> Install the `snscrape` package:
```Python
pip install snscrape
```

# Set Environment
Import the required packages on the pythin notebook/script:
```Python
import snscrape.modules.twitter as sntwitter
import pandas as pd
```
# Extract Data
```Python
query = "State criteria of search"
tweets = [] # Empty list 
limit = 5000 # least number of tweets returned

#Function
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
  if len(tweets) == limit:
    break
  else:
    tweets.append([tweet.date, tweet.user.username, tweet.content])
```
> Store Data:
```Python
df = pd.DataFrame(tweets, columns=["Date", "User", "Tweet"])
```
# Search Criteria
> ## 1. To search tweets of a user:
```Python
```
> ## 2. To search a keyword:
```Python
```
> ## 3. Twitter advanced Search
### Steps
Login [Twitter]() >> Click on the search box >> Type keyword/user of interest >> Press Enter to search

On the __Search filters__ click on the __Advanced search__

Type the `keyword` and the `date range` desires >> Press Enter.

Results:
```Python
```
