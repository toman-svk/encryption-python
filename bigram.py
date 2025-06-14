import numpy as np
import pandas as pd
import re
from collections import defaultdict

with open('./data/krakatit.txt', 'r', encoding='utf-8') as file:
    text = file.read().replace(' ', '_').upper()

text = re.sub(r'[^A-Z_]', '', text)  # filtrovat pismena z ceskej abecedy

unique_chars = sorted(set(text))
char_to_index = {char: idx for idx, char in enumerate(unique_chars)}

# absolutni matice
size = len(unique_chars)
abs_matrix = np.zeros((size, size), dtype=int)
for i in range(len(text) - 1):
    first_char = text[i]
    second_char = text[i + 1]
    if first_char in char_to_index and second_char in char_to_index:
        abs_matrix[char_to_index[first_char], char_to_index[second_char]] += 1

# relativni matice
abs_matrix += 1
total_bigrams = abs_matrix.sum()
rel_matrix = abs_matrix / total_bigrams

# print tabulky matice
df_abs = pd.DataFrame(abs_matrix, index=unique_chars, columns=unique_chars)
df_rel = pd.DataFrame(rel_matrix, index=unique_chars, columns=unique_chars)

# vytvoreni csv dokumentu
df_abs.to_csv('absolutni_bigramova_matice.csv', encoding='utf-8-sig')
df_rel.to_csv('relativni_bigramova_matice.csv', encoding='utf-8-sig')

print("Absolutní a relativní bigramové matice byly úspěšně vytvořeny a uloženy.")
