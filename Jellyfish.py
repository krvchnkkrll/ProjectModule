import jellyfish


for answer in cleaned_answers:
    lev_distance = jellyfish.levenshtein_distance(cleaned_query, answer)
    print(f"Для запроса: {cleaned_query} и ответа: {answer}. \nРасстояние Левенштейна: {lev_distance}")

for answer in cleaned_answers:
    jaro_similarity = jellyfish.jaro_similarity(cleaned_query, answer)
    print(f"Для запроса: {cleaned_query} и ответа: {answer}. \nJaro Similarity: {jaro_similarity:.4f}")

for answer in cleaned_answers:
    jaro_winkler_similarity = jellyfish.jaro_winkler_similarity(cleaned_query, answer)
    print(f"Для запроса: {cleaned_query} и ответа: {answer}. \nJaro-Winkler Similarity: {jaro_winkler_similarity:.4f}")
