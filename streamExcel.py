import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import openpyxl

consumer_key = "nZNaBHqEUFIVNeFBUUjFQWa3c"
consumer_secret= "ltjmhAUnl6xbQa8ZzSW7XkM0heciSoO5YDMoGVjfpaw6nPoENe"
access_token = "124088888-9bFnLQjsZTeGyKiZqYHyQ05ZsJkG9eaD4CywRd08"
access_token_secret = "FXmtMaItnfXvFx5ybO8L6SIwO95TV58dhLmnTxAy01LfN"

''' Create an excel sheet, give it headers'''
wb=openpyxl.Workbook()
s=wb.get_sheet_by_name('Sheet')


currentRow = 1
colNames= ["Name","Tweet","PersonDescription","Following","Followers","statusCount","retweet_count","verified","LocationOfOriginOfTweet","lang"]
s['A1'] = colNames[0]
s['B1'] = colNames[1]
s['C1'] = colNames[2]
s['D1'] = colNames[3]
s['E1'] = colNames[4]
s['F1'] = colNames[5]
s['G1'] = colNames[6]
s['H1'] = colNames[7]
s['I1'] = colNames[8]
s['J1'] = colNames[9]



currentRow = 2

class listener(StreamListener):
  
    def on_status(self, status):
        try:
            tweet = status.user.screen_name + status.text
            #print (tweet)
            #print(type("string"))
            
            print(currentRow)
             
            
            s['A'+str(currentRow)] = str(status.user.screen_name)
            print(s['A'+str(currentRow)].value)
            s['B'+str(currentRow)] = str(status.text)
            s['C'+str(currentRow)] = status.user.description
            s['D'+str(currentRow)] = status.user.friends_count
            s['E'+str(currentRow)] = status.user.followers_count
            s['F'+str(currentRow)] = status.user.statuses_count
            s['G'+str(currentRow)] = status.retweet_count
            
            s['I'+str(currentRow)] = status.user.verified 
            s['J'+str(currentRow)] = status.lang
            
            
            if (type(status.user.location) == type("string")):
                print ("True")
                s['H'+str(currentRow)] = status.user.location
            else:
                print ("False")
                s['H'+str(currentRow)] = "none"
                
                   
            globals()['currentRow']+=1 #This is perhaps the most imp line. Helps your work with global variable.
            wb.save('DegreeDikhaoModiJi.xlsx')

                 
        except : #Called on any exception 
            wb.save('DegreeDikhaoModiJi.xlsx')
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
twitterStream.filter(track=["#DegreeDikhaoModiJi"], async=True)


