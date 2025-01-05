import re
import time

from fuzzywuzzy import fuzz

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
    ratio = fuzz.ratio(query, answer)
    print(f"Для запроса: {query} \nКоэффициент сходства: {ratio}")
print("Коэффициент c учётом сортировки токенов\n\n")

for query in cleaned_queries:
    ratio = fuzz.partial_ratio(query, answer)
    print(f"Для запроса: {query} \nКоэффициент сходства: {ratio}")
print("Коэффициент c учётом сортировки токенов\n\n")

for query in cleaned_queries:
    ratio = fuzz.token_sort_ratio(query, answer)
    print(f"Для запроса: {query}. \nКоэффициент c учётом сортировки токенов: {ratio}")

print("C учётом пересечения множеств токенов\n\n")
for query in cleaned_queries:
    ratio = fuzz.token_set_ratio(query, answer)
    print(f"Для запроса: {query}. \nC учётом пересечения множеств токенов: {ratio}")


print("Partial Token Sort Ratio\n\n")
for query in cleaned_queries:
    ratio = fuzz.partial_token_sort_ratio(query, answer)
    print(f"Для запроса: {query}. \nC учётом пересечения множеств токенов: {ratio}")

print("Partial Token Set Ratio\n\n")
for query in cleaned_queries:
    ratio = fuzz.partial_token_set_ratio(query, answer)
    print(f"Для запроса: {query}. \nC учётом пересечения множеств токенов: {ratio}")

mil_words = get_mil_dictionary()

time1 = time.time()

for word in mil_words:
    fuzz.ratio(answer, word)

time2 = time.time()

print(f"Время выполнения расчёта коэффициента сходства для всех слов словаря:{time2 - time1}")

