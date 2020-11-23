"""Imports"""
"""" counter and matplotlib and tweetpy"""

import  string
from collections import Counter
import matplotlib.pyplot as plt
#my access tokens for twitter and other keys
access_token = '755665303267319809-I6xS6eS9nGcqWPu2KsLPRjcGzNAgo7V'
access_token_secret = 'xVOqqWMOI2n8AWHsy7XS4nhk3BREtKnr437VjSOZ5SBX6'
consumer_key = 'IexkMW7L7HtkBeDw2KHTNqLMU'
consumer_secret = 'L79HyRPnfZrUSfQNLtP6ZO6myGDO3bFaAnnC33dltAU2WcZcd2'
import tweepy
auth_handler = tweepy.OAuthHandler(consumer_key=consumer_key,consumer_secret=consumer_secret)
auth_handler.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth_handler)
#the search term the user wants
search_term = str(input("Enter the tweet you want to search"))
#the amount of tweets that can be searched
tweet_amount = 200
tweets = tweepy.Cursor(api.search,q=search_term,lang='en').items(tweet_amount)
mytweets = []
#preprocessing the tweets to give proper strings
for tweet in tweets:
    final_text = tweet.text.replace('RT','')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
    if final_text.startswith('@'):
        position = final_text.index(' ')
        final_text = final_text[position+2:]
    mytweets.append(final_text)
text = mytweets[0]
#preprocessing the strings
print(text)

lowcase = text.lower()
# print(lowcase)
#Param1: specifies the list of characters that need to be replaced
#Param2: specifies the list of characters with which the characters need to be replaced
#param3: specifies the list of characters that needs to be deleted

clean_text = lowcase.translate(str.maketrans('','',string.punctuation))
# print(clean_text)
tokenize_word = clean_text.split()
# the stopwords which have to be eliminated
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
# final words after preprocessing the data
fword = []
for word in tokenize_word:
    if word not in stopwords:
        fword.append(word)
# print(fword)
#NLP Emotion Algorithm
#1) check if the word is in the fword list is also present in emotions.txt
    #-open the emotion file
    #-loop through each line and clear it
    #-extract the word and emotion using split
#2)-if the word is present add it to emotion_list
emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        print(clear_line[:-1])
        word,emotion = clear_line.split(':')
        # print(word)
        if word in fword:
            emotion_list.append(emotion)
print(emotion_list)
w = Counter(emotion_list)
print(w)
print(text)
fig,axi = plt.subplots()
axi.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()