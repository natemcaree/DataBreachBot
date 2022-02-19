from dotenv import load_dotenv
load_dotenv()
import os
#environment vars




import tweepy
import pandas as pd
import numpy as np
######
import matplotlib.pyplot as plt
import re
import spacy
import seaborn as sns
import snowballstemmer
from pathlib import Path
from records import *

filepath = Path('E:\Desktop\Coding_Projects\Data Breach bot\out.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)


nlp = spacy.load('en_core_web_sm')

######
#Authenticate to Twitter

API_Key = os.getenv("API_KEY")
API_secret_key = os.getenv("API_secret_key")
access_token2 = os.getenv("access_token2")
access_token_secret2 = os.getenv("access_token_secret2")

auth = tweepy.OAuthHandler(API_Key, API_secret_key)
auth.set_access_token(access_token2, access_token_secret2)
api = tweepy.API(auth)


number_of_tweets = 10
tweets = []
likes = []
time = []
searchterm1 = 'Target'
searchterm2 = 'AND data breach'
searchterm3 = 'OR ransomware'
searchterm4 = 'OR cybersecurity'
query = ' '.join([searchterm1, searchterm2, searchterm3, searchterm4])
cursor = tweepy.Cursor(api.search_tweets, q=query, tweet_mode="extended").items(number_of_tweets)


for i in cursor:
    tweets.append(i.full_text)
    #likes.append(i.favorite_count)
    #time.app
    # end(i.created_at)
    
    
            
# s1 = pd.Series(tweets, name = 'tweets')
# s2 = pd.Series(records_companies, name='companies') 

# df = pd.concat([s1, s2], axis=1)

df1 = pd.DataFrame({'tweets' : tweets})
df2 = pd.DataFrame({'companies' : records_companies})

df1 = df1[~df1.tweets.str.contains('RT')]


# df1['overlap'] = [sum(all(val in cell for val in row) for cell in df2['companies']) for row in df1['tweets']]


# idx = np.searchsorted(df1.tweets.values, df2.companies.values)
# df1['overlap'] = df2.companies.values[idx] 


#print(df)
df1.to_csv(filepath)


df1['result'] = df1['tweets'].isin(df2['companies'])
print (df1['result'])

list_of_sentences = [sentence for sentence in df1.tweets]

lines = []
for sentence in list_of_sentences:
    words = sentence.split()
    for w in words:
        lines.append(w)
        
lines = [re.sub(r'/[^A-Za-z0-9]+/', '', x) for x in lines]

lines2 = []

for word in lines:
    if word != '':
        lines2.append(word)



s_stemmer = snowballstemmer.stemmer('english')

stem = []
for word in lines2:
    stem.append(s_stemmer.stemWord(word))
  
stem2 = []    
for word in stem:
    if word not in nlp.Defaults.stop_words:
        stem2.append(s_stemmer.stemWord(word))

df3 = pd.DataFrame(stem2)
df3 = df3[0].value_counts()

df3 = df3[:35,]
plt.figure(figsize=(10,5))
sns.barplot(df3.values, df3.index, alpha=1)
plt.title('Top Words Overall')
plt.ylabel('Word from Tweet', fontsize=12)
plt.xlabel('Count of Words', fontsize=12)
plt.show()

