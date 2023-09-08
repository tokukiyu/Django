import facebook
import requests

access_token = 'EAAEiZAG3Kh08BOxucdrv0avGWYfZCK2RNYO3Nf0cY1JsKZAFsywZA4I61BiZBWH7ZBhre2jZCX00J0uVnVwtsoZCNI1sGIEgCQ8geZCPzcZBvyi4AEF4ta3FZCWAY7bp4owqLHmVorrmTuMvDmJJbMAd02nZC1xeFB1X0zB2ZA1wUCnKgGbaLeuegZBDpCBu9SeI4NpVF9YKk19OAM21s6ZBpDCVLxNewBoOceS' 

url = f"https://graph.facebook.com/v13.0/search?q=%23oromo&type=post&access_token={access_token}"

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
