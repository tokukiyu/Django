import facebook

access_token = "EAAEiZAG3Kh08BOzIgI0ZBOV1NgYTwZAZBvnP01NMpLR8VzCcN2F5df12EWNcfqLbCodU5pj3rXJznkY8wiqh7AjpfHqW8QWp6ZACOXZBGGWpbZAuEvGFEQaBpNFKKgAvj8bFTfKuM68KknEUjgkipzOpxVrZAfjJYoj3fq315v6mSZCgPA1TDM1nrYGflHrYkZAVjU9lZBkQN0UEEZCs75wlDVMZD" 

graph = facebook.GraphAPI(access_token)

fql_query = ("SELECT post_id, permalink, message FROM post WHERE "
             "hashtags IN ('#oromo') AND is_published = true")

fql_result = graph.fql(fql_query) 

for post in fql_result:  
   print(post['post_id'], post['permalink'], post['message'])