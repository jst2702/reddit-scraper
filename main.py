from fastapi import FastAPI
from reddit_scraper.scraping.scrape_reddit import scrape_subreddit
from reddit_scraper.db.crud import read_post

if __name__ == '__main__':
    subreddit = 'computerscience'
    print(scrape_subreddit(subreddit))
    print(read_post(1))
