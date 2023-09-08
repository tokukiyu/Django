import facebook
import urllib.parse 
import requests
#access_token = 'EAAEiZAG3Kh08BO7tvP4nvj9EqG3uZBZBHeTGkfLWVgkHTDuZC2mSuhPE2yKsO6b0WZAsXvhZBrTGj4HMMFrVv6nvfRTPkX0x7Dy4cEjT2OHBvtZAH3pZA1oOGIYYeF2So9HwIEmMaSMIMn6RvMyKG1ivQ3h0mxHj2poxNBqhaJ3meozxcGrWREPvZAJQLS5WgMgljicJxuzwAOLihsLIQiAYYE7YUaZAoZD' 

# Encode the hashtag
hashtag_encoded = urllib.parse.quote('#oromo')

# Construct the API request URL
url = f"https://graph.facebook.com/v17.0/search?q={hashtag_encoded}&type=post&access_token={access_token}"

# Send the GET request to Facebook's Graph API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for post in data.get('data', []):
        print(post.get('message', 'No message'))
        print(post.get('created_time', 'No creation time'))
        print(post.get('id', 'No ID'))
else:
    print(f"Error fetching posts: {response.status_code}")
