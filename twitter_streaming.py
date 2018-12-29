#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "236615876-m1OXUUKmIHmI1lbzPDsbMTg80vfdLgYQUlHmQqOH"
access_token_secret = "mhMIOGA4E9x4dOlzmYLEwS5CWFEqqYWl8bssRFdIExJe9"
consumer_key = "slEk04BQgbsacuSJFZGtIOkZi"
consumer_secret = "dyicjl0xGSU1e4Mv25bMopdjO3FjRXpKyBOCcuLNSs7UXc4F9B"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_status(self, status):
        if hasattr(status, 'retweeted_status'):
            try:
                tweet = status.retweeted_status.extended_tweet['full_text']
                print tweet
            except:
                tweet = status.retweeted_status.text
        else:
            try:
                tweet = status.extended_tweet["full_text"]
                print tweet
            except AttributeError:
                tweet = status.text
                print tweet
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l, tweet_mode="extended")

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['#theoffice'])
