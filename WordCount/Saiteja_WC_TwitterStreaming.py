from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey ='lZDYy4SGH3LzDTVaJTXTpNE32'
csecret ='7sN8DwmOaDVbwzbIPqQ2YD487PFim2dvKfcEBxp1MyGSC4VKRd'
atoken ='1329089202-0ng1VeSSQnVIWyJvJ5QLaUnz0fyzABpzSzjeAw0'
asecret ='mhOaFQDuLjb4QAfSqptd1hNkEqJDKMLsbtBishDQUiVj5'

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
