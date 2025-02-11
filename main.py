import tweepy
import google.generativeai as genai
import os

from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

# Twitter API keys
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
API_KEY = os.getenv("TWEETER_API_KEY")
API_SECRET = os.getenv("TWEETER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWEETER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWEETER_ACCESS_SECRET")

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Setup Twitter Authentication for API v2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

# Setup Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Function to generate a tweet using Gemini
def generate_tweet():
    prompt = "Generate a short, engaging tweet about the latest developments in science and technology. Keep it under 280 characters."
    response = model.generate_content(prompt)
    tweet = response.text.strip()

    if len(tweet) > 280:  # Ensure tweet length is within limits
        tweet = tweet[:277] + "..."  

    print("Generated Tweet:", tweet)
    return tweet

# Function to post a tweet using Twitter API v2
def post_tweet():
    tweet = generate_tweet()
    try:
        client.create_tweet(text=tweet)  # Uses Twitter API v2
        print("Tweet posted successfully!")
    except tweepy.TweepyException as e:
        print("Error posting tweet:", e)

# Schedule the bot to run every 3 hours


print("Bot is running... Tweeting every  hour.")
# Keep running the script

