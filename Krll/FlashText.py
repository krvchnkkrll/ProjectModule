import re
import time

from flashtext import KeywordProcessor

# Инициализация FlashText
keyword_processor = KeywordProcessor()

# Ключевые слова
keywords = ["человек", "сон", "работоспособность", "нужно", "сутки", "спать", "нормально", "чувствовать"]
for keyword in keywords:
    keyword_processor.add_keyword(keyword)

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

# Функция для оценки схожести предложений
def compare_sentences_with_flashtext(query, answer):
    # Извлечение ключевых слов
    query_keywords = set(keyword_processor.extract_keywords(query.lower()))
    answer_keywords = set(keyword_processor.extract_keywords(answer.lower()))

    # Сравнение: пересечение ключевых слов
    common_keywords = query_keywords & answer_keywords
    total_keywords = query_keywords | answer_keywords  # Объединение ключевых слов

    # Оценка схожести
    similarity = len(common_keywords) / len(total_keywords) if total_keywords else 0
    return similarity, query_keywords, answer_keywords


# Поиск наиболее похожего предложения
most_similar_query = None
highest_similarity = 0

for query in queries:
    similarity, query_keywords, answer_keywords = compare_sentences_with_flashtext(query, answer)
    print(f"Запрос: {query}")
    print(f"Ключевые слова запроса: {query_keywords}")
    print(f"Ключевые слова ответа: {answer_keywords}")
    print(f"Схожесть: {similarity:.4f}\n")

    if similarity > highest_similarity:
        highest_similarity = similarity
        most_similar_query = query

# Результат
if most_similar_query:
    print(f"Наиболее похожий запрос: {most_similar_query}")
    print(f"Коэффициент схожести: {highest_similarity:.4f}")
else:
    print("Нет достаточно похожих запросов.")



mil_words = get_mil_dictionary()

time1 = time.time()

for word in mil_words:
    similarity, query_keywords, answer_keywords = compare_sentences_with_flashtext(word, answer)

time2 = time.time()

print(f"Время выполнения расчёта коэффициента сходства для всех слов словаря:{time2 - time1}")