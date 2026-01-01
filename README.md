# CaesarCipher - Simple Console-Based Caesar Cipher

# Caesar Cipher

A simple console-based implementation of the Caesar cipher encryption algorithm in Python. Encrypt and decrypt messages using a shift key.

## Features

-   **Encryption** - Convert plaintext to ciphertext.
-   **Decryption** - Convert ciphertext back to plaintext.
-   **Custom Shift Key** - Choose any shift value (1-25).
-   **Preserves Non-Alphabetic Characters** - Spaces, punctuation, and numbers remain unchanged.
-   **Case Preservation** - Maintains uppercase and lowercase letters.
-   **User-Friendly Interface** - Simple command-line interaction.

## How It Works

The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet. For example, with a shift of 3:

-   A → D
-   B → E
-   C → F
-   ... and so on.

## Installation

### Prerequisites

-   Python 3.6 or higher.

### Setup

1. Clone the repository:

```bash
git clone https://github.com/Balsha98/Repository-CaesarCipher.git
```

2. Navigate to the project directory:

```bash
cd Repository-CaesarCipher/caesar-cipher
```

## Usage

Run the program:

```bash
python main.py
```

## Project Structure

```
CaesarCipher/
│
├── caesar-cipher/      # Main application directory.
│   │
│   ├── assets/         # Application assets.
│   │   │
│   │   ├── data/
│   │   │   └── alphabet.py     # Letters array.
│   │   │
│   │   └── handlers/
│   │       └── methods.py      # Processing methods.
│   │
│   └── main.py         # Application entry point.
│
└── README.md           # Project documentation.
```

## Technical Details

-   **Algorithm**: Caesar cipher (shift cipher).
-   **Character Set**: a-z (26 letters).
-   **Special Characters**: Preserved as-is.
-   **Time Complexity**: O(n) where n is the length of the message.

## Limitations

-   **Not Cryptographically Secure**: Caesar cipher is easily broken with frequency analysis or brute force.
-   **Educational Purpose**: This implementation is for learning and demonstration only.
-   **Limited Character Set**: Only works with English alphabet.

## Educational Resources

The Caesar cipher is one of the oldest and simplest encryption techniques, named after Julius Caesar who used it for military communication. It's an excellent introduction to:

-   Cryptography fundamentals.
-   String manipulation in Python.
-   ASCII character codes.
-   Modular arithmetic.

## Let's Connect

If you enjoyed this project or have any questions, feel free to reach out!

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:balsa.bazovic@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/balsha-bazovich)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Balsha98)

⭐ If you found this project helpful, please consider giving it a star!
