from openai import OpenAI
from reddit import get_subreddit_posts
from os import getenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Free limit: If you are using a free model variant (with an ID ending in :free), then you will be limited to 20 requests per minute and 200 requests per day.

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=getenv("OPENROUTER_API_KEY"),
)


def generate(prompt):
    completion = client.chat.completions.create(
        model="nousresearch/hermes-3-llama-3.1-405b:free",
        messages=[{
            "role": "user",
            "content": prompt
        }])
    return completion.choices[0].message.content


def generate_newsletter(subreddit):
    reddit_content = get_subreddit_posts(subreddit)
    prompt = "You are a professional Newsletter writer. \n" \
    "Given the following reddit posts write a newsletter, that summarizes " \
    "the content of the posts. \n\n" \
    f"{reddit_content} \n\n" \
    "Format the output as if it was the body of an email. Omit the subject line.\n" \
    "Omit any additional output. Include urls to the respective posts."
    return generate(prompt)
