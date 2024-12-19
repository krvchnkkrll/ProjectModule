from difflib import SequenceMatcher

from fuzzywuzzy import fuzz
from rapidfuzz import fuzz as rf_fuzz
from rapidfuzz.distance import Jaro, JaroWinkler
from Levenshtein import distance, ratio, hamming
from thefuzz import fuzz as tf_fuzz

str1 = 'Мама мыла раму.'
str2 = 'Мама мыла большую раму.'
fuzz_ratio = fuzz.ratio(str1, str2)

fuzzy_partial_ratio = fuzz.partial_ratio(str1, str2)
fuzzy_token_sort_ratio = fuzz.token_sort_ratio(str1, str2)
fuzzy_token_set_ratio = fuzz.token_set_ratio(str1, str2)

# RapidFuzz

rapid_ratio = rf_fuzz.ratio(str1, str2)
rapid_partial_ratio = rf_fuzz.partial_ratio(str1, str2)
rapid_token_sort_ratio = rf_fuzz.token_sort_ratio(str1, str2)
rapid_token_set_ratio = rf_fuzz.token_set_ratio(str1, str2)
rapid_jaro = Jaro.similarity(str1, str2)
rapid_jaro_winkler = JaroWinkler.similarity(str1, str2)

# difflib

difflib_ratio = SequenceMatcher(None, str1, str2).ratio()

# Thefuzz

thefuzz_ratio = tf_fuzz.ratio(str1, str2)
thefuzz_partial_ratio = tf_fuzz.partial_ratio(str1, str2)
thefuzz_token_sort_ratio = tf_fuzz.token_sort_ratio(str1, str2)
thefuzz_token_set_ratio = fuzz.token_set_ratio(str1, str2)

# Levenshtein

levenshtein_distance = distance(str1, str2)
levenshtein_ratio = ratio(str1, str2)
str_lev1 = 'Мама мыла раму.'
str_lev2 = 'Мама мылО раму.'
if len(str_lev1) == len(str_lev2):
    hamming_distance = hamming(str_lev1, str_lev2)
else:
    hamming_distance = "Не применимо для строк разной длины"

print("FuzzyWuzzy:")
print(f"Коэффициент сходства: {fuzz_ratio}")
print(f"Частичное сходство (для подстрок): {fuzzy_partial_ratio}")
print(f"C учётом сортировки токенов: {fuzzy_token_sort_ratio}")
print(f"C учётом пересечения множеств токенов: {fuzzy_token_set_ratio}\n")

print("RapidFuzz:")
print(f"Коэффициент сходства: {rapid_ratio}")
print(f"Частичное сходство (для подстрок):: {rapid_partial_ratio}")
print(f"C учётом сортировки токенов: {rapid_token_sort_ratio}")
print(f"C учётом пересечения множеств токенов: {rapid_token_set_ratio}")
print(f"Сходство Жаро: {rapid_jaro}")
print(f"Сходство Жаро-Винклера: {rapid_jaro_winkler}\n")

print("difflib:")
print(f"Коэффициент сходства: {difflib_ratio}")

print("Thefuzz:")
print(f"Коэффициент сходства: {thefuzz_ratio}")
print(f"Частичное сходство (для подстрок):: {thefuzz_partial_ratio}")
print(f"C учётом сортировки токенов: {thefuzz_token_sort_ratio}")
print(f"C учётом пересечения множеств токенов: {thefuzz_token_set_ratio}\n")

print("Levenshtein:")
print(f"Коэффициент сходства: {levenshtein_distance}")
print(f"Коэффициент сходства: {levenshtein_ratio}")
print(f"Расстояние Хэмминга: {hamming_distance}")
