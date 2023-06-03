def shamir_three_step_encryption(message, p, KAe, KBe):
    Kda = pow(KAe, -1, p - 1)
    # Kdb = pow(KBe, -1, p - 1)
    C1 = pow(message, KAe, p)
    C2 = pow(C1, KBe, p)
    C3 = pow(C2, Kda, p)
    # C4 = pow(C3, Kdb, p)
    return C3


message = 47
p = 751
KAe = 739
KBe = 577

ciphertext = shamir_three_step_encryption(message, p, KAe, KBe)
print("Cipher text:", ciphertext)


message = 806
p = 839
KAe = 155
KBe = 207

ciphertext = shamir_three_step_encryption(message, p, KAe, KBe)
print("Cipher text:", ciphertext)


def attack_shamir_with_verman(hex_str1, hex_str2):
    int1 = int(hex_str1, 16)
    int2 = int(hex_str2, 16)
    result = int1 ^ int2
    hex_result = hex(result)[2:].upper()

    return hex_result


# Messages sent
message_1 = "212E6838DE9DAE0"  # A -> B
message_2 = "06022FCAF509C4C"  # B -> A
message_3 = "1BC968898D8BA18"  # A -> B

# result = attack_shamir_with_verman(attack_shamir_with_verman(message_1, message_2), message_3)
# print("Original text:", result)

