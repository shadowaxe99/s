
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import load_model

class ContentCuration:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.vectorizer = TfidfVectorizer(stop_words=self.stop_words)
        self.model = load_model('../models/ai_model.h5')

    def preprocess_text(self, text):
        text = text.lower()
        tokenized_text = nltk.word_tokenize(text)
        filtered_text = [word for word in tokenized_text if word not in self.stop_words]
        return ' '.join(filtered_text)

    def predict_category(self, text):
        preprocessed_text = self.preprocess_text(text)
        text_vector = self.vectorizer.transform([preprocessed_text])
        prediction = self.model.predict(text_vector)
        return prediction.argmax(axis=-1)

    def curate_content(self, text):
        category = self.predict_category(text)
        return category
