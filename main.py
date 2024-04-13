from fastapi import FastAPI
from reddit_scraper.scraping.scrape_reddit import scrape_subreddit
from reddit_scraper.db.crud import read_post
app = FastAPI()

@app.get("/scrape")
def scrape(subreddit: str):
    num_posts = scrape_subreddit(subreddit)
    return f"{num_posts} posts scraped from {subreddit}"

@app.get("/post/{post_id}")
def get_post(post_id: int):
    # Assuming you have a function to retrieve a post by its ID
    # Replace the function name and implementation accordingly
    post = read_post(post_id)
    if post:
        return post
    else:
        return {"error": "Post not found"}