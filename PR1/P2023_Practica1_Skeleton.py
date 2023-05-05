#!/usr/bin/env python3
# -*- coding: utf-8 -*-



ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:?"



# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed
from random import randint

KEY_NUMBER = 7

# ----------------------------------------------------------------------------




def uoc_rotative_encrypt(message, shift):
    """
    EXERCISE 1: Simple substitution cipher
    :message: message to cipher (plaintext)
    :shift: offset or displacement
    :return: ciphered text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####
    # Iterate for each letter in the message to encrypt
    for letter in message:
        # Add the letter to the ciphertext, but we add the shift number
        # to the letter in the ABC as a reference.
        # Usage of the modulo to avoid going out of the ABC range
        ciphertext += ABC[(ABC.index(letter) + shift) % len(ABC)]
    # --------------------------------

    return ciphertext




def uoc_rotative_decrypt(message, shift):
    """
    EXERCISE 2: Simple substitution decipher
    :message: message to cipher (plaintext)
    :shift: offset or displacement
    :return: ciphered text
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####
    # Iterate for each letter in the message to encrypt
    for letter in message:
        # Add the letter to the ciphertext, but we rest the shift number
        # to the letter in the ABC as a reference.
        # Usage the modulo to avoid going out of the ABC range
        plaintext += ABC[(ABC.index(letter) - shift) % len(ABC)]
    # --------------------------------

    return plaintext




def uoc_grille_genkey(grille_len, num_holes):
    """
    EXERCISE 3: Key generation
    :gruille_len: total grille length in symbols
    :num_holes: Number of holes in the grille
    :return: key as list of 0 and 1
    """

    key = []

    #### IMPLEMENTATION GOES HERE ####
    # A while loop is started and will continue until the key is filled
    while len(key) < grille_len:
        # A random number is generated and added to the key.
        # If the sum of the key is equal to the number of holes, a 0 is added
        key.append(randint(0, 1)) if sum(key) != num_holes else key.append(0)
        # If the key is filled and the sum of the key is not equal to the number
        # of holes, the key is emptied and the while loop will start again
        if len(key) == grille_len and sum(key) != num_holes:
            key = []
    # --------------------------------

    return key




def uoc_grille_encrypt(key, plaintext):
    """
    EXERCISE 4: Encrypt a text using the key
    :message: message to grille_encrypt
    :shift: offset or displacement
    :return: ciphered text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####
    # A variable is created to count the number of letters from the plaintext
    # are covered
    letters_covered = 0
    # A while loop is started and will continue until all the letters from the
    # plaintext are covered
    while letters_covered < len(plaintext):
        # A for loop is started to iterate for each letter in the key
        for grille in key:
            # If all the letters from the plaintext are covered, the while loop
            # is broken
            if letters_covered == len(plaintext):
                break
            # If the key is 1, the letter in the plaintext is added to the
            # ciphertext and the number of letters covered is increased
            if grille == 1:
                ciphertext += plaintext[letters_covered]
                letters_covered += 1
            # If the key is 0, a random letter from the ABC is added to the
            # ciphertext
            else:
                ciphertext += ABC[randint(0, len(ABC) - 1)]
    # --------------------------------

    return ciphertext




def uoc_grille_decrypt(key, ciphertext):
    """
    EXERCISE 5: Decrypt a text using the key
    :message: message to grille_decrypt
    :subs_alphabet: substitution alphabet
    :return: ciphered text
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####
    # A for loop is started to iterate for each letter in the ciphertext
    for position in range(len(ciphertext)):
        # If the key is 1, the letter in the ciphertext is added to the
        # plaintext
        if key[position % len(key)] == 1:
            plaintext += ciphertext[position]
    # --------------------------------

    return plaintext




def uoc_encrypt(key, plaintext):
    """
    EXERCISE 6: Complete cryptosystem (encrypt)
    :key: grille key
    :plaintext: message to encrypt
    :return: encrypted text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####
    # We encrypt the plaintext with the rotative cipher
    rotative_encrypted_text = uoc_rotative_encrypt(plaintext, KEY_NUMBER)
    # We encrypt the rotative encrypted text with the grille cipher
    ciphertext = uoc_grille_encrypt(key, rotative_encrypted_text)
    # --------------------------------

    return ciphertext




def uoc_decrypt(key, ciphertext):
    """
    EXERCISE 6: Complete cryptosystem (decrypt)
    :key: grille key
    :ciphertext: message to decrypt
    :return: plaintext
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####
    # We decrypt the ciphertext with the grille cipher
    rotative_decrypted_text = uoc_grille_decrypt(key, ciphertext)
    # We decrypt the rotative decrypted text with the rotative cipher
    plaintext = uoc_rotative_decrypt(rotative_decrypted_text, KEY_NUMBER)
    # --------------------------------

    return plaintext
