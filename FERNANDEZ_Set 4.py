#!/usr/bin/env python
# coding: utf-8

# In[9]:


def bin_to_dec(binary_string):

    binary_length = len(binary_string)
    converted_binary = 0

    for i in range(0, binary_length):
        converted_binary += int(binary_string[i]) * (2 ** (binary_length - 1 - i))

    return converted_binary

bin_to_dec("101")


# In[10]:


def dec_to_bin(number):

    converted_number = ""
    
    if number == 0:
        return "0"
    
    else: 
        while number != 0:
        
            if number % 2 == 1:
                converted_number = "1" + converted_number

            elif number % 2 == 0:
                converted_number = "0" + converted_number

            number = number // 2

        return converted_number

dec_to_bin(255)


# In[11]:


encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }

def telephone_cipher(message):
   
    message_length = len(message)
    converted_message = encoder_dict[(message[0])]

    for i in range(1, message_length):
        
        if converted_message[-1] == encoder_dict[(message[i])][0]:
            converted_message += ("_" + encoder_dict[(message[i])])

        else:
            converted_message += encoder_dict[(message[i])]

    return converted_message

telephone_cipher("ABRACADABRA")


# In[12]:


decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }

def telephone_decipher(telephone_string):
   
    string_length = len(telephone_string)
    telephone_message = ""
    i = 0

    while i != string_length:

        if telephone_string[i] == "_":
            i += 1
            continue

        j = i
        while j != string_length and telephone_string[j] == telephone_string[i]:
            j += 1
        
        telephone_message += decipher_dict[telephone_string[i:j]]
        
        i = j

    return telephone_message

telephone_decipher("4433555_555666096667775553")

