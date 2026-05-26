import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

texts = [
    "AI is very useful for students",
    "Technology improves education",
    "Machine learning helps society",
    "AI can create new opportunities",
    "I support artificial intelligence",
    "AI is dangerous for jobs",
    "Technology creates unemployment",
    "Artificial intelligence is risky",
    "I do not trust AI systems",
    "Machines may replace humans"
]

labels = [1,1,1,1,1,0,0,0,0,0]

model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])

model.fit(texts, labels)

os.makedirs('models', exist_ok=True)

joblib.dump(model, 'models/sentiment_model.pkl')

print("Model trained successfully!")