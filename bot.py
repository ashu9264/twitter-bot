import tweepy
consumer_key='rsxDz5vS4jVlyfA8ia2uz5w9Y'
consumer_secret='cJiW4oY1oDUuLaktsEltLYuUcN7huy1xnnHaEKBl5DbiPr22wQ'
access_token='3228598200-Ti74xbrFlqJHSDSvi6QfTwVfqG7UUMxWts4BQlE'
access_token_secret='wRzyKkBYXbZTl5ihV03l8PAZGFYTyNs8VaKOZ2dQ3p2gz'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
auth.secure=True
api=tweepy.API(auth,wait_on_rate_limit=True)

#user_id=input('Enter your Twitter User id :')

print('Total Followers:\n')
for user in tweepy.Cursor(api.followers, '@ashurenu1993').items():
    print (user.screen_name)
    
print('\n')

print('Total Followings:\n')
for user in tweepy.Cursor(api.friends, '@ashurenu1993').items():
    print (user.screen_name)
    
print('\n')

tweets = api.user_timeline(screen_name = '@boltiot', count=1)
for tweet in tweets:
    
    try:
        if(tweet.favorited==False):
            tweet.favorite()
    except tweepy.TweepError as e:
        
        if(e.reason=="[{'code': 139, 'message': 'You have already favorited this status.'}]"):
            continue 
        
    except StopIteration:
        break
    
print('#boltiot Tweet Liked \n\n#IOT like begins..... ')

for tweet in tweepy.Cursor(api.search,q='#IOT').items(10):
    
    try:
        if(tweet.favorited==False):
            
            tweet.favorite()
            
            
            
    except tweepy.TweepError as e:
        
        if(e.reason=="[{'code': 139, 'message': 'You have already favorited this status.'}]"):
            continue 
        
    except StopIteration:
        break



    


    


    
    
