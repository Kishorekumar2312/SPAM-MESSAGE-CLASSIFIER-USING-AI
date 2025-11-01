"""Training script: trains a Naive Bayes spam classifier and saves model/vectorizer.

This file previously contained embedded CSS/HTML/JS and a Flask app. Those
assets have been moved to `static/` and `templates/` and a standalone `app.py`
was added. Keep this script for training only.
"""

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import os


# === 1. Load the dataset ===
import os
data_path = os.path.join(os.path.dirname(__file__), 'data', 'spam.csv')
data = pd.read_csv(data_path, encoding='latin-1')
print("✅ CSV loaded successfully!")
print(data.head())

# The Kaggle dataset has extra unnamed columns, so we clean it
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

# === 2. Preprocess labels ===
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# === 3. Split into train/test ===
X_train, X_test, y_train, y_test = train_test_split(
    data['message'], data['label'], test_size=0.2, random_state=42
)

# === 4. Convert text to numeric form ===
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# === 5. Train Naive Bayes model ===
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# === 6. Test accuracy ===
y_pred = model.predict(X_test_vec)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))

# === 7. Save model and vectorizer ===
os.makedirs('model', exist_ok=True)

with open('model/spam_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("🎉 Model and vectorizer saved successfully!")

# For the web app, see `app.py` and the created `templates/` and `static/` files.
