from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time
import re

# Данные
queries = [
    "Cколько часов челавеку нужно спать в утки чтобы нормально себя чуствовать и быть роботоспособным?",
    "Чтобы нормально себя чувствовать и быть работоспособным, cколько часов человеку нужно спать в сутки?",
    "Сколько часов человеку нужно спать чтобы оставаться работоспособным?",
    "Человеку нужно питаться минимум 3-4 раза в сутки, чувствовать себя сильным."
]

answer = "Сколько часов человеку нужно спать в сутки, чтобы нормально себя чувствовать и быть работоспособным?"

def clean_sentence(sentence):
    return re.sub(r'[^\w\s]', '', sentence).lower()


def get_mil_dictionary():
    words = []
    with open('../million_words.txt', 'r',
              encoding='utf-8') as f:
        for line in f:
            words.append(line.strip())
    return words

# Преобразование текстов в векторы с использованием TF-IDF
vectorizer = TfidfVectorizer()
all_texts = queries + [answer]  # Объединяем запросы и ответ

# Создаём матрицу TF-IDF
tfidf_matrix = vectorizer.fit_transform(all_texts).toarray()

# Вектор ответа
answer_vector = tfidf_matrix[-1]

# Вычисление косинусного сходства
cosine_similarities = []
for query_vector in tfidf_matrix[:-1]:
    similarity = cosine_similarity([answer_vector], [query_vector])[0, 0]
    cosine_similarities.append(similarity)

# Результаты
results = []
for idx, similarity in enumerate(cosine_similarities):
    results.append({"query": queries[idx], "similarity": similarity})

# Вывод результатов
for result in results:
    print(f"Запрос: {result['query']}")
    print(f"Косинусное сходство: {result['similarity']:.4f}\n")

# Измерение времени работы TF-IDF для слов из словаря
mil_words = get_mil_dictionary()
word_vectors = vectorizer.transform(mil_words).toarray()

# Время выполнения с использованием TF-IDF и косинусного сходства
start_time_tfidf = time.time()
cosine_similarities = []
for word_vector in word_vectors:
    similarity = cosine_similarity([answer_vector], [word_vector])[0, 0]
    cosine_similarities.append(similarity)
end_time_tfidf = time.time()

print(f"Время выполнения расчёта косинусного сходства для всех слов словаря: {end_time_tfidf - start_time_tfidf:.4f} секунд")
