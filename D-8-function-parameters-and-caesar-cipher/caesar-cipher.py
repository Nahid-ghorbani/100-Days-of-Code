alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet_len = len(alphabet)

def encrypt(original_text, shift_amount):
    cipher_text = ''
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= alphabet_len #we use % so basically there is no limit for shift number
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        original_position = alphabet.index(letter) - shift_amount % alphabet_len
        cipher_text += alphabet[original_position]
    print(f"Here is the decoded result: {cipher_text}")

def caesar():
    if direction == "encode":
        encrypt(text, shift)
    elif direction =="decode":
        decrypt(text, shift)

caesar()