import re
import time
from difflib import SequenceMatcher

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
    ratio = SequenceMatcher(None, query, answer).ratio()
    print(f"Для запроса: {query} и ответа: {answer}. \nКоэффициент сходства: {ratio}")


mil_words = get_mil_dictionary()

time1 = time.time()

for word in mil_words:
    SequenceMatcher(None, answer, word).ratio()

time2 = time.time()

print(f"Время выполнения расчёта коэффициента сходства для всех слов словаря:{time2-time1}")
