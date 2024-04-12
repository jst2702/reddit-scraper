import sqlite3
from reddit_scraper.db.metadata import DB_PATH
from reddit_scraper.db.classes import Post

def create_post(post):
    """
    Create a new post in the database.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO posts (title, author) VALUES (?, ?)''', (post.title, post.author))
    conn.commit()
    conn.close()

def read_posts():
    """
    Retrieve all posts from the database.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''SELECT * FROM posts''')
    posts = [Post(title=row[1], author=row[2]) for row in c.fetchall()]
    conn.close()
    return posts

def update_post(post_id, new_post):
    """
    Update an existing post in the database.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''UPDATE posts SET title = ?, author = ? WHERE id = ?''', (new_post.title, new_post.author, post_id))
    conn.commit()
    conn.close()

def delete_post(post_id):
    """
    Delete a post from the database.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''DELETE FROM posts WHERE id = ?''', (post_id,))
    conn.commit()
    conn.close()
