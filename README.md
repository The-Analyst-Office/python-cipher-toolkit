# Python Cipher Toolkit

An interactive Python application for encoding and decoding messages using two classical cryptographic techniques: Caesar Cipher and Vigenère Cipher.

## Features

- Encode and decode messages using Caesar Cipher.
- Encode and decode messages using Vigenère Cipher.
- Interactive command-line menu.
- Input validation for shift amounts and keywords.
- Ability to perform multiple operations in one session.
- Support for uppercase message input through lowercase conversion.

## How to Run

1. Ensure Python 3 is installed.
2. Download `python_cipher_toolkit.py`.
3. Open a terminal in the folder containing the file.
4. Run:

   `python python_cipher_toolkit.py`

5. Follow the on-screen instructions.

## Example

**Cipher:** Caesar Encode  
**Message:** hello  
**Shift:** 3  
**Output:** ebiil

## Project Background

This project began with Codecademy's *Coded Correspondence* exercises. I expanded the original cipher functions into an interactive Python application with menus, input validation, repeat functionality, and improved user-facing messages.

## Limitations

- Messages are converted to lowercase.
- Vigenère keywords must contain lowercase English letters only.
- Caesar and Vigenère are classical educational ciphers and are not suitable for securing sensitive information.

## Technologies

- Python 3
- Jupyter Notebook (development and testing)