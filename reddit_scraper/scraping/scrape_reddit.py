import requests
from reddit_scraper.db import create_post, Post

def scrape_subreddit(subreddit: str) -> int:
    url = f'https://www.reddit.com/r/{subreddit}.json'

    print(f"scraping: {url}", flush=True)

    response = requests.get(url)
    body = response.json()

    num_posts = 0
    for data in body['data']['children']:
        title = data['data']['title']
        author = data['data']['author_fullname']
        
        post = Post(title, author)
        create_post(post)
        num_posts += 1
    return num_posts
