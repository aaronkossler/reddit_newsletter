import praw
import json
from os import getenv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

reddit = praw.Reddit(client_id=getenv("REDDIT_CLIENT_ID").strip(),
                     client_secret=getenv("REDDIT_CLIENT_SECRET").strip(),
                     user_agent=getenv("REDDIT_USER_AGENT").strip(),
                     username=getenv("REDDIT_USER").strip(),
                     password=getenv("REDDIT_PASS").strip())


def get_subreddit_posts(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    result = {}
    if os.path.exists("ids.json"):
        with open("ids.json", "r") as file:
            ids = json.load(file)
    else:
        ids = []
    submissions = [
        submission for submission in subreddit.top(limit=20, time_filter="day")
        if id not in ids
    ]
    ids = []
    for submission in submissions:
        ids.append(submission.id)
        result[submission.id] = {
            "title":
            submission.title,
            "url":
            submission.url,
            "score":
            submission.score,
            "content":
            submission.selftext
            if submission.is_self else submission.url  # Grabs selftext or URL
        }
    dump_ids(ids)
    return result


def dump_ids(ids):
    with open('ids.json', 'w') as file:
        json.dump(ids, file)
