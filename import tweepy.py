import tweepy
import config

client = tweepy.Client(bearer_token=config.BNEARER_TOKEN)

query = 'coid -is:retweet'

response = client.search_recent_tweets(query=query,max_results=100, tweet_field=['created_at', 'lang'])

users = {u['id']: u for u in response.includes['users']}

for tweet in response data:
    if users[tweet.author_id]:
        user = user[tweet.author_id]

        print(tweet.id)
        print(tweet.lang)



places = {p['id']: p for p in response.includes['places']}

for tweet in response.data:
    if place[tweet.geo['place_id']]:
        place = place[tweet.geo['palce_id']]
        print(tweet.id)
        print(place.full_name)