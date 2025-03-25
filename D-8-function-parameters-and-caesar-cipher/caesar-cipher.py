alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet_len = len(alphabet)

def encrypt(original_text, shift_amount):
    encrypted_text = ''
    for letter in original_text:
        letter_index = alphabet.index(letter)
        new_index = letter_index + shift_amount
        if new_index > alphabet_len:
            new_index -= alphabet_len
        new_letter = alphabet[new_index]
        encrypted_text += new_letter

    print(encrypted_text)

if direction == "encode":
    encrypt(text, shift)


