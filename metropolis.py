import random
from encrypt import encrypt
from decrypt import decrypt
import pandas as pd
from smart_keygen import generate_initial_key
import numpy as np
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"

# Load the reference bigram matrix
# reference = pd.read_csv('relativni_bigramova_matice.csv', index_col=0).values
# reference += 1e-10  # to avoid log(0)
# Generate smarter initial key from frequency analysis

def bigram_score(text, bigram_matrix, alphabet=ALPHABET):
    score = 0
    text = text.upper()
    for i in range(len(text) - 1):
        a, b = text[i], text[i + 1]
        if a in alphabet and b in alphabet:
            i1, i2 = alphabet.index(a), alphabet.index(b)
            score += np.log(bigram_matrix[i1][i2])
    return score

def random_key():
    return ''.join(random.sample(ALPHABET, len(ALPHABET)))

def swap_two_chars(s):
    s = list(s)
    i, j = random.sample(range(len(s)), 2)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)

def metropolis_hastings(ciphertext, reference_matrix, iterations=10000, initial_key=None):
    # Improve the decryption using smart key generation
    initial_key = generate_initial_key(ciphertext)
    current_key = initial_key if initial_key else random_key()
    current_decryption = decrypt(ciphertext, current_key)
    current_score = bigram_score(current_decryption, reference_matrix)

    best_key = current_key
    best_score = current_score
    score_history = []

    for _ in range(iterations):
        candidate_key = swap_two_chars(current_key)
        candidate_decryption = decrypt(ciphertext, candidate_key)
        candidate_score = bigram_score(candidate_decryption, reference_matrix)

        # M-H acceptance criteria
        if candidate_score > current_score or random.random() < np.exp(candidate_score - current_score):
            current_key = candidate_key
            current_score = candidate_score
            if candidate_score > best_score:
                best_key = candidate_key
                best_score = candidate_score

        score_history.append(best_score)

    return best_key, score_history