# File containing code for XOR ciphers
import secrets
from inputrefactor import yes_no_input

# Basis for this cipher is contained in this proof
# x ^ 0 = x   --> x ^ 0 ^ 0 = x
# x ^ 1 = ~x  --> x ^ 1 ^ 1 = x


def xor_operation(message, key) -> int:
    return message ^ key


def xor_cipher():
    input_number = int(input("Input a number between 0 and 256: "))
    print("Generating random key...")
    key = secrets.randbits(8)
    cipher_message = xor_operation(input_number, key)
    print("Your encrypted message:", cipher_message, end="\n\n")
    
    repeat_yes_no: bool = yes_no_input("Would you like to see your number deciphered? (y/n): ")
    if repeat_yes_no:
        print("Your deciphered input:", xor_operation(cipher_message, key))

xor_cipher()