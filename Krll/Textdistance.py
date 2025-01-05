import textdistance
import re
import time

queries = [
    "Cколько часов челавеку нужно спать в утки чтобы нормально себя чуствовать и быть роботоспособным?",
    "Чтобы нормально себя чувствовать и быть работоспособным, cколько часов человеку нужно спать в сутки?",
    "Сколько часов человеку нужно спать чтобы оставаться работоспособным?"
]

answer = "Сколько часов человеку нужно спать в сутки, чтобы нормально себя чувствовать и быть работоспособным?"

def get_mil_dictionary():
    words = []
    with open('../million_words.txt', 'r',
              encoding='utf-8') as f:
        for line in f:
            words.append(line.strip())
    return words

def clean_sentence(sentence):
    return re.sub(r'[^\w\s]', '', sentence).lower()


cleaned_queries = []

cleaned_answer = clean_sentence(answer)

for query in queries:
    cleaned_queries.append(clean_sentence(query))


for query in cleaned_queries:
    hamming = textdistance.hamming.normalized_similarity(cleaned_answer, query)
    print(f"Для запроса: {query} и ответа: {cleaned_answer}.")
    print(f"Hamming Similarity: {hamming:.4f}")

    levenshtein = textdistance.levenshtein.normalized_similarity(cleaned_answer, query)
    print(f"Для запроса: {query} и ответа: {cleaned_answer}.")
    print(f"Levenshtein Similarity: {levenshtein:.4f}")

    jaccard = textdistance.jaccard.normalized_similarity(cleaned_answer, query)
    print(f"Для запроса: {query} и ответа: {cleaned_answer}.")
    print(f"Jaccard Similarity: {jaccard:.4f}")


mil_words = get_mil_dictionary()

time1 = time.time()

for word in mil_words:
    hamming = textdistance.hamming.normalized_similarity(cleaned_answer, word)
    levenshtein = textdistance.levenshtein.normalized_similarity(cleaned_answer, word)
    jaccard = textdistance.jaccard.normalized_similarity(cleaned_answer, word)

time2 = time.time()

print(f"Время выполнения расчёта коэффициента сходства для всех слов словаря:{(time2 - time1)/3}")