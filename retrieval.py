from pathlib import Path
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self):
        self.records = json.loads((Path(__file__).parent / 'data/schemes.json').read_text(encoding='utf-8'))
        self.vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform([f"{r['scheme']} {r['category']} {r['question']} {r['answer']}" for r in self.records])

    def search(self, question, category='All'):
        scores = cosine_similarity(self.vectorizer.transform([question]), self.matrix)[0]
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        return [dict(self.records[i], score=round(float(scores[i]), 4)) for i in ranked if scores[i] >= 0.08 and (category == 'All' or self.records[i]['category'] == category)][:3]
