from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Define training texts and their corresponding labels[cite: 3]
texts = [
    "I love this course",
    "This course is excellent",
    "I hate this course",
    "This course is terrible",
]

labels = [
    "positive",
    "positive",
    "negative",
    "negative",
]

# Convert text into numerical features using CountVectorizer[cite: 2, 3]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train a Naive Bayes text classification model[cite: 3]
model = MultinomialNB()
model.fit(X, labels)

# Generate a prediction for new unseen text during inference[cite: 2, 3]
new_text = ["I really love this course"]
new_X = vectorizer.transform(new_text)
prediction = model.predict(new_X)

print("New Text:", new_text[0])
print("Prediction:", prediction[0])