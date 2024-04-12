from fastapi import FastAPI
from reddit_scraper.scraping.scrape_reddit import scrape_subreddit

app = FastAPI()

@app.get("/scrape")
def scrape(subreddit: str):
    num_posts = scrape_subreddit(subreddit)
    return f"{num_posts} posts scraped from {subreddit}"