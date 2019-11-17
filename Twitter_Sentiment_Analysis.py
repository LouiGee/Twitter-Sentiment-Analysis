import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
import sys, tweepy
#Pulling data from twitter API


def percentage(part, whole):
    return 100* float(part)/float(whole)


#Establish connection with API
consumerKey = 'RsbnQsbT4iqTig1DUQpFxQMmZ'
consumerSecret = 'NFC36EqSYW8eCQoBf3nQDtcvhuR7ZoLPKc5sriKtYYbLDOLDQB'
accessToken = '545456317-iDwUPui245CDG2rvmVCngprsLmhqaBtsOiAaKETG'
accessTokenSecret = '7vtapH1ZGVqzJ2teN7wTiOVDK4nCeF215Uscs4TNAzy8q'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Input
searchterm = input("Enter keyword/hashtag to search about: ")
noOfSearchterms = int(input('Enter how many tweets to analyse: '))

#Variable holding the tweets
tweets = tweepy.Cursor(api.search, q =searchterm).items(noOfSearchterms)


#Three variables to store the polarity 

positive = 0
negative = 0
neutral = 0
polarity = 0 #Average of the tweets


for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    
    if (analysis.sentiment.polarity == 0):
        neutral +=1
    elif (analysis.sentiment.polarity > 0.00):
        positive +=1
    elif (analysis.sentiment.polarity < 0.00):
        negative +=1
                
        
positive = percentage(positive, noOfSearchterms)
negative = percentage(negative, noOfSearchterms)
neutral = percentage(neutral, noOfSearchterms)

positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')

labels = ['Positve ['+str(positive)+'%]', 'Neutral [' + str(neutral) +'%]', 'Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colours = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors=colours, startangle=90)
plt.legend(patches, labels, loc='best')
plt.title('How people are reacting on '+searchterm+' by analysing '+str(noOfSearchterms)+' Tweets.')
plt.axis('equal')
plt.tight_layout()    


