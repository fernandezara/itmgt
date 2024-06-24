#!/usr/bin/env python
# coding: utf-8

# In[1]:


def shift_letter(letter, shift):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter == " ":
        new_letter = " "

    elif alphabet.index(letter) + shift <= 25:
        new_letter = alphabet[alphabet.index(letter) + shift]

    else:
        new_index = alphabet.index(letter) + shift - 26

        while new_index > 25:
            new_index = new_index - 26

        new_letter = alphabet[new_index]

    return new_letter

shift_letter(" ",104)


# In[26]:


def caesar_cipher(message, shift):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_length = len(message)
    letter_index = 0
    new_message = ""

    while message_length != letter_index:
        letter = message[letter_index]
        letter_index += 1

        if letter == " ":
            new_message += " "

        elif alphabet.index(letter) + shift <= 25:
            new_message += alphabet[alphabet.index(letter) + shift]

        else:
            new_index = alphabet.index(letter) + shift - 26

            while new_index > 25:
                new_index = new_index - 26

            new_message += alphabet[new_index]

    return new_message

caesar_cipher ("HELLO WORLD", 2)


# In[19]:


def shift_by_letter(letter, letter_shift):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter == " ":
        new_letter = " "

    elif alphabet.index(letter) + alphabet.index(letter_shift) <= 25:
        new_letter = alphabet[alphabet.index(letter) + alphabet.index(letter_shift)]

    else:
        new_index = alphabet.index(letter) + alphabet.index(letter_shift) - 26

        while new_index > 25:
            new_index = new_index - 26

        new_letter = alphabet[new_index]

    return new_letter

shift_by_letter("B","K")


# In[160]:


def vigenere_cipher(message, key):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_length = len(message)
    letter_index = 0
    new_message = ""

    # new key 

    key_index = 0
    new_key = (len(message) // len(key)) * key

    if key_index <= len(message) // len(key):

        while key_index != (len(message) % len(key)):
            new_key += key[key_index]
            key_index = key_index + 1

    # shifting the message
    
    while message_length != letter_index:
        letter = message[letter_index]
        shift = new_key[letter_index]
        letter_index += 1

        if letter == " ":
            new_message += " "

        elif alphabet.index(letter) + alphabet.index(shift) <= 25:
            new_message += alphabet[alphabet.index(letter) + alphabet.index(shift)]

        else:
            new_index = alphabet.index(letter) + alphabet.index(shift) - 26

            while new_index > 25:
                new_index = new_index - 26

            new_message += alphabet[new_index]

    return new_message

vigenere_cipher("A C", "KEY")


# In[229]:


def scytale_cipher(message, shift):

    #checking the length
    
    new_message = message

    if len(message) % shift != 0:
        new_message += ((shift - (len(message) % shift)) * "_")

    #shifting the message

    message_length = len(new_message)
    letter_index = 0
    final_message = ""

    while message_length != letter_index:
        new_index = (letter_index // shift) + (len(new_message) // shift) * (letter_index % shift)
        final_message += new_message[new_index]

        letter_index += 1

    return final_message

scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8)


# In[254]:


def scytale_decipher(message, shift):
    
    message_length = len(message)
    letter_index = 0
    final_message = ""

    while message_length != letter_index:
        new_index = (letter_index % (len(message) // shift)) * shift + (letter_index // (len(message) // shift))
        final_message += message[new_index]

        letter_index += 1

    return final_message

scytale_decipher("IMNNA_FTAOIGROE", 3)

