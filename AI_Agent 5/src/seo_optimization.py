
import nltk
from nltk.corpus import stopwords
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

class SEOOptimizer:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def keyword_extraction(self, text):
        words = nltk.word_tokenize(text)
        words = [word for word in words if word.isalnum() and word not in self.stop_words]
        frequency = Counter(words)
        return frequency.most_common(10)

    def tf_idf(self, documents):
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(documents)
        feature_names = vectorizer.get_feature_names_out()
        dense = vectors.todense()
        denselist = dense.tolist()
        df = pd.DataFrame(denselist, columns=feature_names)
        return df
