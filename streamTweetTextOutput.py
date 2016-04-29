import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os




fo = open("dataRevAll.txt", "w")

#print(type("Name"+"|"+"Tweet"+"|"+"PersonDescription"+"|"+"Following"+"|"+"Followers"+"|"+"statusCount"+"|"+"retweet_count"+"|"+"verified"+"|"+"LocationOfOriginOfTweet"+"|"+"lang"))

fo.write(str("Name"+"|"+"Tweet"+"|"+"PersonDescription"+"|"+"Following"+"|"+"Followers"+"|"+"statusCount"+"|"+"retweet_count"+"|"+"verified"+"|"+"LocationOfOriginOfTweet"+"|"+"lang")+ str(os.linesep))
'''
status.user.screen_name
status.text
status.user.description
status.user.location -- not accurate
status.user.verified (true or false)
status.user.followers_count
--status.user.created_at
status.user.statuses_count
status.retweet_count
status.user.friends_count
---
status.place -- gives data sometimes, doesn't other times.
status.place.country -- not working
status.place.full_name-- not
status.place.name -- not
status.place.place_type --not
status.place.url -- not
--Doesn't work -- status.coordinates.coordinates (longitude and latitude)
'''

class listener(StreamListener):
    
    ''' On status worked better than on_data. The json format can be directly used here '''
   
    def on_status(self, status):
        try:
            tweet = status.user.screen_name+ status.text
            print (tweet)
            #print(type("string"))
            ''' Below if else is required since location object is not always present '''
            if (type(status.user.location) == type("string")):
                print ("True")
                fo.write(str(status.user.screen_name)+"|"+str(status.text)+"|"+str(status.user.description)+"|"+str(status.user.friends_count)+"|"+str(status.user.followers_count)+"|"+str(status.retweet_count)+"|"+str(status.user.verified)+"|"+str(status.user.location)+"|"+str(status.lang)+ str(os.linesep))
            else:
                print ("False")
                fo.write(str(status.user.screen_name)+"|"+str(status.text)+"|"+str(status.user.description)+"|"+str(status.user.friends_count)+"|"+str(status.user.followers_count)+"|"+str(status.retweet_count)+"|"+str(status.user.verified)+"|"+str("none")+"|"+str(status.lang)+ str(os.linesep))
     

        except : #Called on any exception
            
            print ('failed on data'),str(e)
            #time.sleep(2)
    on_event = on_status

    def on_error(self, status):
        print (status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
''' Wait for the input '''
#__track = raw_input("Enter something you want to track: ")
twitterStream = Stream(auth, listener())
''' Enter the string that needs to be tracked '''
twitterStream.filter(track=["pussy"], async=True)
