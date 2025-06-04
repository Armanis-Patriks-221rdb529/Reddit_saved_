import credentials
import praw

def fethcdata():
    reddit = praw.Reddit(
        client_id = credentials.CLIENT_ID,
        client_secret = credentials.SECRET,  
        user_agent = credentials.AGENT,
        username = credentials.USERNAME,                       
        password = credentials.PASSWORD
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
                    elif any(p in i for p in ('gallery', 'v.redd')):
                        g.write(i + "\n")
                    else:
                        a.write(i + "\n")
                    