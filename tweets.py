import requests
import json
from requests_oauthlib import OAuth1
Consumer_Key='afcB58TdOAfsBgaiTzdYbzvPL'
Consumer_Secret='I0CAM68ikunSSd99cX8X5r6CaZEC08GNKEzp1EkCjI6kc2xArS'
Access_Token ='1011198782065635329-tqi6WW2GIn0u9m1qevJ7o0TZaGikaw'
Access_Token_Secret ='Q2BeZZEhH57jzBIATOwjHmzUr3cTvjTdcyFSTXH8mmqvW' 
username=raw_input("enter the username:")
url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&tweet_mode=extended"
auth = OAuth1(Consumer_Key,Consumer_Secret,Access_Token, Access_Token_Secret)
r=requests.get(url,auth=auth)
#print r
d=r.json()
#print d
for t in d:
 print t['full_text']

