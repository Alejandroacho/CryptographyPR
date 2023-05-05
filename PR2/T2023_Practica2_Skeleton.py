#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES

MODE_CIPHER = 0
MODE_DECIPHER = 1

# --- IMPLEMENTATION GOES HERE ---------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed
def xor(x, y):
    return x ^ y


def rotate(lfsr: list, polynomial: list):
    first_element = 0
    for index in range(len(polynomial)):
        if polynomial[index] == 1:
            first_element = xor(lfsr[index], first_element)
    lfsr.pop()
    lfsr.insert(0, first_element)
# --------------------------------------------------------------------------


def uoc_lfsr_sequence(polynomial, initial_state, output_bits):
    """
    Returns the output sequence of output_bits bits of an LFSR with a given initial state and connection polynomial.

    :param polynomial: list of integers, with the coefficients of the connection polynomial that define the LFSR.
    :param initial_state: list of integers with the initial state of the LFSR
    :param output_bits: integer, number of bits of the output sequence
    :return: a list of output_bits bits
    """
    result = None

    # --- IMPLEMENTATION GOES HERE ---
    result = None

    # --- IMPLEMENTATION GOES HERE ---
    result = []
    # we reverse the given arrays
    initial_state.reverse()
    polynomial.reverse()
    # we copy the initial state to a new array
    lfsr = initial_state.copy()
    # we rotate the lfsr as many times as output_bits and we append the last element to the result
    for _ in range(output_bits):
        result.append(lfsr[-1])
        rotate(lfsr, polynomial)
    # --------------------------------

    return result


def uoc_ext_a5_pseudo_random_gen(params_pol_0, params_pol_1, params_pol_2, clocking_bits, output_bits):
    """
    Implements extended A5's pseudorandom generator.
    :param params_pol_0: two-element list describing the first LFSR: the first element contains a list with the
    coefficients of the connection polynomial, the second element contains a list with the initial state of the LFSR.
    :param params_pol_1: two-element list describing the second LFSR: the first element contains a list with the
    coefficients of the connection polynomial, the second element contains a list with the initial state of the LFSR.
    :param params_pol_2: two-element list describing the third LFSR: the first element contains a list with the
    coefficients of the connection polynomial, the second element contains a list with the initial state of the LFSR.
    :param clocking_bits: three-element list, with the clocking bits of each LFSR
    :param output_bits: integer, number of bits of the output sequence
    :return: list of output_bits elements with the pseudo random sequence
    """

    sequence = []

    # --- IMPLEMENTATION GOES HERE ---
    # we create the 3 LFSRs
    lfsr_1 = uoc_lfsr_sequence(params_pol_0[0], params_pol_0[1], len(params_pol_0[1]))
    lfsr_2 = uoc_lfsr_sequence(params_pol_1[0], params_pol_1[1], len(params_pol_1[1]))
    lfsr_3 = uoc_lfsr_sequence(params_pol_2[0], params_pol_2[1], len(params_pol_2[1]))

    # we reverse the given arrays to work with them as stacks
    lfsr_1.reverse()
    lfsr_2.reverse()
    lfsr_3.reverse()

    # we rotate the lfsr as many times as output_bits and we append the last element to the result
    for _ in range(output_bits):
        #  we apply xor between the last 3 elements of the LFSRs
        output = xor(xor(lfsr_1[-1], lfsr_2[-1]), lfsr_3[-1])
        sequence.append(output)
        clock_bit_val1 = lfsr_1[clocking_bits[0]]
        clock_bit_val2 = lfsr_2[clocking_bits[1]]
        clock_bit_val3 = lfsr_3[clocking_bits[2]]

        #  We only rotate the LFSRs in the following cases:
        # - If the clocking bits of the 3 LFSRs are equal
        if clock_bit_val1 == clock_bit_val2 == clock_bit_val3:
            rotate(lfsr_1, params_pol_0[0])
            rotate(lfsr_2, params_pol_1[0])
            rotate(lfsr_3, params_pol_2[0])
        # - If the clocking bits of the first val is different from the rest
        elif clock_bit_val1 != clock_bit_val2 == clock_bit_val3:
            rotate(lfsr_2, params_pol_1[0])
            rotate(lfsr_3, params_pol_2[0])
        # - If the clocking bits of the second val is different from the rest
        elif clock_bit_val1 == clock_bit_val3 != clock_bit_val2:
            rotate(lfsr_1, params_pol_0[0])
            rotate(lfsr_3, params_pol_2[0])
        # - If the clocking bits of the third val is different from the rest
        elif clock_bit_val1 == clock_bit_val2 != clock_bit_val3:
            rotate(lfsr_1, params_pol_0[0])
            rotate(lfsr_2, params_pol_1[0])
    # --------------------------------

    return sequence


def uoc_a5_cipher(initial_state_0, initial_state_1, initial_state_2, message, mode):
    """
    Implements ciphering/deciphering with the A5 pseudo random generator.

    :param initial_state_0: list, initial state of the first LFSR
    :param initial_state_1: list, initial state of the second LFSR
    :param initial_state_2: list, initial state of the third LFSR
    :param message: string, plaintext to cipher (mode=MODE_CIPHER) or ciphertext to decipher (mode=MODE_DECIPHER)
    :param mode: MODE_CIPHER or MODE_DECIPHER, whether to cipher or decipher
    :return: string, ciphertext (mode=MODE_CIPHER) or plaintext (mode=MODE_DECIPHER)
    """

    output = ""

    # --- IMPLEMENTATION GOES HERE ---
    params_pol_0 = [[1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], initial_state_0]
    params_pol_1 = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], initial_state_1]
    params_pol_2 = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], initial_state_2]
    clocking_bits = [8, 10, 10]

    # We are in cipher mode, so we receive plain text
    if mode == MODE_CIPHER:
        # We convert the message to binary
        bytes_array = [byte for byte in bytearray(message, 'utf-8')]
        binary_array = [format(byte, '08b') for byte in bytes_array]
        binary_result = ''.join(binary_array)
        # We parse the binary string to a list of integers
        message_list = list(map(int, binary_result))
        # We get the output bits by the length of the message
        outputs_bit = len(message_list)
        # We generate a new key with the output bits
        key = uoc_ext_a5_pseudo_random_gen(params_pol_0, params_pol_1, params_pol_2, clocking_bits, outputs_bit)
        # Finally we iterate each element of generated key and the message bits to get the ciphered message with xor
        for index in range(outputs_bit):
            output += str(xor(message_list[index], key[index]))

    # We are in decipher mode, received binary str
    else:
        # We parse the binary string to a list of integers
        message_list = list(map(int, message))
        # We get the output bits by the length of the message
        outputs_bit = len(message_list)
        # We generate a new key with the output bits
        key = uoc_ext_a5_pseudo_random_gen(params_pol_0, params_pol_1, params_pol_2, clocking_bits, outputs_bit)
        # We create a string to store the result
        binary_str_result = ''
        # Finally we iterate each element of generated key and the message bits to get the deciphered message with xor
        for i in range(outputs_bit):
            binary_str_result += str( xor(message_list[i], key[i]))
        # We convert the binary string to a integer and then to a string
        integer = int(binary_str_result, base=2)
        # We convert the integer to a bytes
        string = integer.to_bytes((integer.bit_length() + 7) // 8, 'big')
        # We decode the bytes to a string
        output = string.decode()
    # --------------------------------

    return output


def uoc_aes(message, key):
    """
    Implements 1 block AES enciphering using a 256-bit key.

    :param message: string of 1 and 0s with the binary representation of the messsage, 128 char. long
    :param key: string of 1 and 0s with the binary representation of the key, 256 char. long
    :return: string of 1 and 0s with the binary representation of the ciphered message, 128 char. long
    """

    cipher_text = ""

    # --- IMPLEMENTATION GOES HERE ---
    # We create an hex string from the key
    hex_key_str = hex(int(key, base=2))[2:]
    # We create bytes from the hex string
    binary_key_str = bytes.fromhex(hex_key_str)
    # We create an AES object with the bytes
    cipher_key = AES.new(binary_key_str, AES.MODE_ECB)
    # We create an hex string from the key
    hex_message_str = hex(int(message, base=2))[2:]
    # We create bytes from the hex string
    binary_message_str = bytes.fromhex(hex_message_str)
    # we encrypt the given message. the output is in bytes (hex)
    bytes_hex_cipher = cipher_key.encrypt(binary_message_str)
    # We convert the bytes to a hex string
    hex_cipher = bytes_hex_cipher.hex()
    # We convert the hex string to a binary string
    binary = bin(int(hex_cipher, 16))
    # We remove the first two characters of the binary string
    cipher_text = binary[2:].zfill(128)
    # --------------------------------

    return cipher_text


def uoc_g(message):
    """
    Implements the g function.

    :param message: string of 1 and 0s with the binary representation of the messsage, 128 char. long
    :return: string of 1 and 0s, 256 char. long
    """

    output = ""

    # --- IMPLEMENTATION GOES HERE ---
    # We concatenate the message with itself
    output = message + message
    # --------------------------------

    return output


def uoc_naive_padding(message, block_len):
    """
    Implements a naive padding scheme. As many 0 are appended at the end of the message
    until the desired block length is reached.

    :param message: string with the message
    :param block_len: integer, block length
    :return: string of 1 and 0s with the padded message
    """

    output = ""

    # --- IMPLEMENTATION GOES HERE ---
    # We convert the message to binary
    binary = "".join([bin(ord(i))[2:].zfill(8) for i in message])
    # We add 0 to the right to match the block length expected
    output = binary.ljust(block_len, '0')
    # --------------------------------

    return output


def uoc_mmo_hash(message):
    """
    Implements the hash function.

    :param message: a char. string with the message
    :return: string of 1 and 0s with the hash of the message
    """

    h_i = ""

    # --- IMPLEMENTATION GOES HERE ---
    # We create the requested lfsr
    hash = bin(int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", 16))[2:].zfill(8)
    # We convert the message to binary
    binary_message = ''.join(format(x, '08b') for x in bytearray(message, 'utf-8'))
    # We create a variable to store the chunks (128 bits)
    chunks = 128
    # We get the range of the chunks with the length of the message
    chunk_range = range(chunks, len(binary_message) + chunks, chunks)
    # We chunk the message in chunks of 128 bits
    chunked_messages = [binary_message[chunk - chunks:chunk] for chunk in chunk_range]
    # We apply the crypto system to each chunk
    for chunked_message in chunked_messages:
        # We apply a padding if the chunk is not 128 bits
        if len(chunked_message) < chunks:
            integer = int(chunked_message, base=2)
            string = integer.to_bytes((integer.bit_length() + 7) // 8, 'big').decode()
            chunked_message = uoc_naive_padding(string, chunks)
        # We apply the block cypher function to the chunk
        ciphered = uoc_aes(chunked_message, uoc_g(hash))
        output = ""
        # We apply xor to each bit of the ciphered message and the hash
        for index in range(len(ciphered)):
            output += str(xor(int(ciphered[index]), int(hash[index])))
        hash = output
    h_i = output
    # --------------------------------

    return h_i


def uoc_collision(prefix):
    """
    Generates collisions for uoc_mmo_hash, with messages having a given prefix.

    :param prefix: string, prefix for the messages
    :return: 2-element tuple, with the two strings that start with prefix and have the same hash.
    """

    collision = ("", "")

    # --- IMPLEMENTATION GOES HERE ---



    # --------------------------------

    return collision
