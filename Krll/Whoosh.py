from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser
import os

schema = Schema(content=TEXT(stored=True))


def create_index(index_dir, data):
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)

    ix = create_in(index_dir, schema)
    writer = ix.writer()
    for line in data:
        writer.add_document(content=line)
    writer.commit()
    return ix


def find_most_similar(ix, queries, answer):
    parser = QueryParser("content", schema=ix.schema)
    with ix.searcher() as searcher:
        parsed_answer = parser.parse(answer)
        result_scores = []

        for query in queries:
            parsed_query = parser.parse(query)
            results = searcher.search(parsed_answer, limit=None)

            score = 0
            for r in results:
                if r["content"] == query:
                    score += 1

            result_scores.append((query, score))

    return sorted(result_scores, key=lambda x: x[1], reverse=True)[0][0]


queries = [
    "Cколько часов челавеку нужно спать в утки чтобы нормально себя чуствовать и быть роботоспособным?",
    "Чтобы нормально себя чувствовать и быть работоспособным, cколько часов человеку нужно спать в сутки?",
    "Сколько часов человеку нужно спать чтобы оставаться работоспособным?"
]

answer = "Сколько часов человеку нужно спать в сутки, чтобы нормально себя чувствовать и быть работоспособным?"

index_dir = "indexdir"
data = queries + [answer]
ix = create_index(index_dir, data)

most_similar_query = find_most_similar(ix, queries, answer)
print("Наиболее похожий запрос:", most_similar_query)
