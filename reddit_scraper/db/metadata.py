from reddit_scraper.db import __file__ as f
import os

DB_PATH = os.path.join(os.path.dirname(f), 'posts.db')