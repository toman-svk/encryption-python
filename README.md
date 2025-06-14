# Encryption-Python

This project provides tools for encrypting and decrypting text using classical ciphers, with a focus on bigram analysis and the Metropolis-Hastings algorithm for cryptanalysis. It is designed for educational and research purposes in the field of classical cryptography.

## Features
- Encrypt and decrypt text files using substitution ciphers
- Analyze text using bigram frequency matrices
- Break ciphers using the Metropolis-Hastings algorithm
- Smart key generation for improved decryption
- Jupyter notebooks for interactive experimentation

## Project Structure
- `bigram.py` — Bigram analysis utilities
- `encrypt.py` — Functions for encrypting text
- `decrypt.py` — Functions for decrypting text
- `metropolis.py` — Metropolis-Hastings cryptanalysis implementation
- `smart_keygen.py` — Smart key generation for decryption
- `decrypting.ipynb`, `testing.ipynb` — Jupyter notebooks for experiments
- `data/` — Sample texts, ciphertexts, plaintexts, and keys
- `absolutni_bigramova_matice.csv`, `relativni_bigramova_matice.csv` — Bigram frequency matrices

## Usage

### 1. Encrypting Text
Use `encrypt.py` to encrypt plaintext files with a random or specified key.

### 2. Decrypting Text
Use `decrypt.py` or the Jupyter notebooks to attempt decryption. The Metropolis-Hastings algorithm in `metropolis.py` can be used to break substitution ciphers using bigram statistics.

### 3. Running Notebooks
Open `decrypting.ipynb` or `testing.ipynb` in Jupyter to run experiments and visualize results.

## Requirements
- Python 3.8+
- numpy
- pandas

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Example
To decrypt a ciphertext using the Metropolis-Hastings algorithm:
```python
from metropolis import metropolis_hastings
from decrypt import decrypt

best_key, score_history, _ = metropolis_hastings(ciphertext, reference_matrix)
plaintext = decrypt(ciphertext, best_key)
```

## License
This project is licensed under the MIT License.