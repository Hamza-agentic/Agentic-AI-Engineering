
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def run_advanced_classification():
    # Load dataset from data folder
    df = pd.read_csv("Week 3/data/Support_Ticket.csv")
    
    texts = df["message"]
    labels = df["label"]

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        texts,
        labels,
        test_size=0.25,
        random_state=42,
        stratify=labels
    )

    # Convert text into TF-IDF features
    vectorizer = TfidfVectorizer()
    X_train_vectors = vectorizer.fit_transform(X_train)
    X_test_vectors = vectorizer.transform(X_test)

    # Train a Logistic Regression classifier
    model = LogisticRegression()
    model.fit(X_train_vectors, y_train)

    # Generate predictions and evaluate
    predictions = model.predict(X_test_vectors)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Model Accuracy: {accuracy:.2f}\n")
    print("Classification Report:")
    print(classification_report(y_test, predictions))

    # Test with a new custom query
    new_text = ["My fee payment is missing"]
    new_vectors = vectorizer.transform(new_text)
    prediction = model.predict(new_vectors)

    print(f"New text: {new_text[0]}")
    print(f"Prediction: {prediction[0]}")

if __name__ == "__main__":
    run_advanced_classification()