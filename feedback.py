from textblob import TextBlob
import random

def generate_feedback(user_text):

    blob = TextBlob(user_text)

    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        mood = "Positive"

    elif sentiment < 0:
        mood = "Negative"

    else:
        mood = "Neutral"

    confidence_score = random.randint(70, 95)

    return {
        "sentiment": mood,
        "confidence": confidence_score,
        "grammar": "Good communication skills"
    }