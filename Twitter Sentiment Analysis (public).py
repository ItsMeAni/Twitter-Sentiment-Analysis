from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
def percentage(part, whole):
 if (whole == 0):
     return 0
 return 100 * float(part)/float(whole)

consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
searchTerm = input("Enter keyword/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))
tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)
positive = 0
negative = 0
neutral = 0
polarity = 0
count = 0
for tweet in tweets:
 analysis = TextBlob(tweet.text)
 count += 1
 polarity +=  analysis.sentiment.polarity
 if (analysis.sentiment.polarity > 0.00):
  positive += 1
 elif (analysis.sentiment.polarity == 0):
  neutral += 1
 elif (analysis.sentiment.polarity < 0.00):
  negative += 1

print("Count of tweets: " + str(count))
print("Positive tweets: " + str(positive))
print("Neutral tweets: " + str(neutral))
print("Negative tweets: " + str(negative))
total = positive + negative + neutral
positive = percentage(positive, total)
neutral = percentage(neutral, total)
negative = percentage(negative, total)

positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')

print("How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerms)+" tweets.")

print("General sentiment:")
if (positive >= negative):
    if (positive >= neutral):
        print("Positive")

if (neutral >= negative):
    if (neutral >= positive):
        print("Neutral")

if (negative >= positive):
    if (negative >= neutral):
        print("Negative")

lables = ['Positive ['+str(positive)+'%]', 'Neutral[' +str(neutral)+'%]', 'Negative[' +str(negative)+'%]']
sizes = [positive,neutral,negative]
colors = ['greenyellow', 'tomato', 'darkred']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, lables, loc="best")
plt.title('How people are reacting on '+searchTerm+' by analyzing '+str(noOfSearchTerms)+' tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
