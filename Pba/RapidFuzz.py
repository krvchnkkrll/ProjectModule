import re
import time

from rapidfuzz import fuzz as rf_fuzz
from rapidfuzz.distance import Jaro, JaroWinkler

queries = [
    "Cколько часов челавеку нужно спать в утки чтобы нормально себя чуствовать и быть роботоспособным?",
    "Чтобы нормально себя чувствовать и быть работоспособным, cколько часов человеку нужно спать в сутки?",
    "Сколько часов человеку нужно спать чтобы оставаться работоспособным?"

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


cleaned_queries = []

cleaned_answer = clean_sentence(answer)

for query in queries:
    cleaned_queries.append(clean_sentence(query))

for query in cleaned_queries:
    ratio = rf_fuzz.ratio(query, answer)
    print(f"Для запроса: {query} и ответа: {answer}. \nКоэффициент сходства: {ratio}")

for query in cleaned_queries:
    ratio = rf_fuzz.token_sort_ratio(query, answer)
    print(f"Для запроса: {query} и ответа: {answer}. \nКоэффициент c учётом сортировки токенов: {ratio}")


for query in cleaned_queries:
    ratio = Jaro.similarity(query, answer)
    print(f"Для запроса: {query} и ответа: {answer}. \nСходство Жаро: {ratio}")

for query in cleaned_queries:
    ratio = JaroWinkler.similarity(query, answer)
    print(f"Для запроса: {query} и ответа: {answer}. \nСходство Жаро-Винклера: {ratio}")

mil_words = get_mil_dictionary()

time1 = time.time()

for word in mil_words:
    rf_fuzz.ratio(answer, word)

time2 = time.time()

print(f"Время выполнения расчёта коэффициента сходства для всех слов словаря:{time2-time1}")