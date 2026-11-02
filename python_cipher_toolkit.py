#!/usr/bin/env python
# coding: utf-8

# In[1]:


def caesar_decode(message, offset):
    """Decode a message using a Caesar cipher with the specified shift."""
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    decoded = ''
    for a in message:
        if a not in alphabets:
            decoded += a
        else:
            decoded += (alphabets[(alphabets.index(a)+offset)%len(alphabets)])
    return decoded


def caesar_encode(message, offset):
    """Encode a message using a Caesar cipher with the specified shift."""
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    encoded = ''
    for a in message:
        if a not in alphabets:
            encoded += a
        else:
            encoded += (alphabets[(alphabets.index(a)-offset)%len(alphabets)])
    return encoded

def vigenere_decode(message, keyword):
    """Decode a message using a Vigenère cipher and keyword."""
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    decoded = ''
    counter = 0
    for a in range(len(message)):
        if message[a] not in alphabets:
            decoded += message[a]
        else:    
            decoded += (alphabets[(alphabets.index(message[a])+alphabets.index(keyword[counter % len(keyword)]))%len(alphabets)])
            counter += 1
    return decoded


def vigenere_encode(message, keyword):
    """Encode a message using a Vigenère cipher and keyword."""
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    encoded = ''
    counter = 0
    for a in range(len(message)):
        if message[a] not in alphabets:
            encoded+=message[a]
        else:    
            encoded += (alphabets[(alphabets.index(message[a])-alphabets.index(keyword[counter % len(keyword)]))%len(alphabets)])
            counter += 1
    return encoded

again = 'yes'
while again == 'yes':
    print('Welcome to Python Cipher Toolkit!')
    print('Choosing a cipher:')
    print ('1. Caesar Cipher')
    print('2. Vigenère Cipher')
    print()
    choice = input('Enter 1 for Caesar Cipher or 2 for Vigenère Cipher:')
    print()
    if choice == '1':
        print('You selected Caesar Cipher')
        print()
        print('What would you like to do?')
        print('1. Encode a message')
        print ('2. Decode a message')
        print()
        action = input("Enter 1 to Encode or 2 to Decode: ")
        if action == '1':
            print('great! you want to encode!')
            user_message = input('Enter the message you want to encode: ')
            try:
                shift_amount = int(input('Enter the shift amount (0–25): '))
                if shift_amount in range(26):
                    print('Your message encoded: ',caesar_encode(user_message,shift_amount))
                else:
                    print("Invalid shift amount. Please enter a number between 0 and 25.")
            except ValueError:
                print("Invalid input. Please enter a whole number between 0 and 25.")                           
        elif action == '2':
            print('super! you want to decode')
            user_message = input('Enter the message you want to decode: ')
            try:
                shift_amount = int(input('Enter the shift amount (0–25): '))
                if shift_amount in range(26):    
                    print('Your message decoded: ',(caesar_decode(user_message,shift_amount)))
                else: 
                    print("Invalid shift amount. Please enter a number between 0 and 25.")
            except ValueError:
                print("Invalid input. Please enter a whole number between 0 and 25.")                           
        else:
            print('oooops! that was an invalid choice')
    elif choice == '2':
        print ('You selected Vigenère Cipher')
        print('What would you like to do?')
        print('1. Encode a message')
        print ('2. Decode a message')
        action = input("Enter 1 to Encode or 2 to Decode: ")
        if action == '1':
            print('great! you want to encode!')
            user_message = input('Enter the message you want to encode: ').lower()
            keyword = input('Enter your keyword: ')
            if keyword and all(letter in 'abcdefghijklmnopqrstuvwxyz' for letter in keyword):
                print('Your message encoded: ',(vigenere_encode(user_message,keyword)))
            else:
                print("Invalid keyword. Please enter a non-empty keyword containing only lowercase letters (a–z).")
        elif action == '2':
            print('super! you want to decode')
            user_message = input('Enter the message you want to decode: ').lower()
            keyword = input('Enter your keyword: ')
            if keyword and all(letter in 'abcdefghijklmnopqrstuvwxyz' for letter in keyword):
                print('Your message decoded: ',(vigenere_decode(user_message,keyword)))
            else:
                print("Invalid keyword. Please enter a non-empty keyword containing only lowercase letters (a–z).")
        else:
            print('oooops! that was an invalid choice. Please enter 1 or 2')
    else:
        print ('ermmmm..Invalid choice. Please enter 1 or 2')
    again = input('Would you like to use the toolkit again? (yes/no): ').strip().lower()
    while again not in ('yes', 'no'):
        print("Invalid input. Please enter 'yes' or 'no'.")
        again = input('Would you like to use the toolkit again? (yes/no): ').strip().lower()
print("Thank you for using Python Cipher Toolkit. Goodbye!")



# In[ ]:





# In[ ]:




