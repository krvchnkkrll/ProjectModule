import jellyfish
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
    lev_distance = jellyfish.levenshtein_distance(cleaned_answer, query)
    max_length = max(len(cleaned_answer), len(query))
    similarity_coefficient = 1 - (lev_distance / max_length)
    print(f"Для запроса: {query} и ответа: {cleaned_answer}.")
    print(f"Расстояние Левенштейна: {lev_distance}")
    print(f"Коэффициент схожести (нормализованный Левенштейн): {similarity_coefficient:.4f}")

for query in cleaned_queries:
    jaro_similarity = jellyfish.jaro_similarity(cleaned_answer, query)
    print(f"Для запроса: {query} и ответа: {answer}. \nJaro Similarity: {jaro_similarity:.4f}")

for query in cleaned_queries:
    jaro_winkler_similarity = jellyfish.jaro_winkler_similarity(cleaned_answer, query)
    print(f"Для запроса: {query} и ответа: {answer}. \nJaro-Winkler Similarity: {jaro_winkler_similarity:.4f}")

mil_words = get_mil_dictionary()

time1 = time.time()

for word in mil_words:
    jaro_winkler_similarity = jellyfish.jaro_winkler_similarity(word, query)

time2 = time.time()

print(f"Время выполнения расчёта коэффициента сходства для всех слов словаря:{time2 - time1}")