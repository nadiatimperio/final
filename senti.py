Credit: http://nealcaren.web.unc.edu/

from __future__ import division
import csv
from string import punctuation

tweets = open("breaksns.txt").read()
tweets_list = tweets.split('\n')

pos_sent = open("positive.txt").read()
positive_words=pos_sent.split('\n')
positive_counts=[]

neg_sent = open('negative.txt').read()
negative_words=neg_sent.split('\n')
negative_counts=[]

for tweet in tweets_list:
    positive_counter=0
    negative_counter=0
    
    tweet_processed=tweet.lower()
       
    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')

    words=tweet_processed.split(' ')
    word_count=len(words)
    for word in words:
        if word in positive_words:
            positive_counter=positive_counter+1
        elif word in negative_words:
            negative_counter=negative_counter+1
        
    positive_counts.append(positive_counter/word_count)
    negative_counts.append(negative_counter/word_count)

print len(positive_counts)

output=zip(tweets_list,positive_counts,negative_counts)

writer = csv.writer(open('tweet_sentimentt.csv', 'wb'))
writer.writerows(output)
