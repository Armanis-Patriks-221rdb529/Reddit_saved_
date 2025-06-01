import user
import praw
import requests
from PIL import Image


reddit = praw.Reddit(
    client_id = user.CLIENT_ID,
    client_secret = user.SECRET,  
    user_agent = user.AGENT,
    username = user.USERNAME,                       
    password = user.PASSWORD
)


url_array = []

for item in reddit.user.me().saved(limit=None):
    url_array.append(item.url)

with open("saved_posts.txt", "w") as f:
    with open("gallery_and_mp4.txt", "w") as g:
        with open("misc.txt", "w") as a:
            for i in url_array:
                if any(s in i for s in ('.png', '.jpg', '.jpeg', '.webp')):
                    f.write(i + "\n")
                elif any(p in i for p in ('gallery', '.it')):
                    g.write(i + "\n")
                else:
                    a.write(i + "\n")