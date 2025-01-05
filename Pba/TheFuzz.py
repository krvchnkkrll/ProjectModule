import re
import time

from thefuzz import fuzz as tf_fuzz

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

cleaned_queries = []

cleaned_answer = clean_sentence(answer)

for query in queries:
    cleaned_queries.append(clean_sentence(query))
print("Коэффициент сходства\n\n")
for query in cleaned_queries:
    ratio = tf_fuzz.ratio(query, cleaned_answer)
    print(f"Для запроса: {query}. \nКоэффициент сходства: {ratio}")

print("Частичное сходство (для подстрок)\n\n")
for query in cleaned_queries:
    partial_ratio = tf_fuzz.partial_ratio(query, cleaned_answer)
    print(f"Для запроса: {query}. \nЧастичное сходство (для подстрок): {partial_ratio}")

print("Коэффициент c учётом сортировки токенов\n\n")
for query in cleaned_queries:
    token_sort_ratio = tf_fuzz.token_sort_ratio(query, cleaned_answer)
    print(f"Для запроса: {query}. \nКоэффициент c учётом сортировки токенов: {token_sort_ratio}")

print("C учётом пересечения множеств токенов\n\n")
for query in cleaned_queries:
    token_set_ratio = tf_fuzz.token_set_ratio(query, cleaned_answer)
    print(f"Для запроса: {query}. \nC учётом пересечения множеств токенов: {token_set_ratio}")

# Методы partial_token_sort_ratio, partial_token_set_ratio отсутствуют

mil_words = get_mil_dictionary()

time1 = time.time()

for word in mil_words:
    tf_fuzz.ratio(cleaned_answer, word)

time2 = time.time()

print(f"Время выполнения расчёта коэффициента сходства для всех слов словаря:{time2-time1}")


