import requests
from reddit_scraper.db import create_post, Post

def scrape_subreddit(subreddit: str) -> int:
    response = requests.get(f'https://www.reddit.com/r/{subreddit}.json')
    body = response.json()

    num_posts = 0
    for data in body['data']['children']:
        author = data['data']['author_fullname']
        title = data['data']['title']
        
        post = Post(title, author)
        create_post(post)
        num_posts += 1
    return num_posts
