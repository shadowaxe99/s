
import tensorflow as tf
from tensorflow.keras.models import load_model
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

class ContentReview:
    def __init__(self):
        self.model = load_model('../models/ai_model.h5')
        self.vectorizer = TfidfVectorizer()

    def preprocess_text(self, text):
        tokens = word_tokenize(text)
        return " ".join([word.lower() for word in tokens if word.isalpha()])

    def review_content(self, text):
        preprocessed_text = self.preprocess_text(text)
        vectorized_text = self.vectorizer.transform([preprocessed_text])
        prediction = self.model.predict(vectorized_text)
        return prediction

if __name__ == "__main__":
    review = ContentReview()
    text = "Sample text for review"
    print(review.review_content(text))
