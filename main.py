alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    if shift > 26:
        shift = shift % 26

    if direction == "encode":
        encrypted = ''

        for letter in text:
            location = alphabet.index(letter)
            new_location = location + shift
            encrypted += alphabet[new_location]
        print(f"The encoded text is {encrypted}")

    if direction == "decode":
        decrypted = ''

        for letter in text:
            location = alphabet.index(letter)
            new_location = location - shift
            decrypted += alphabet[new_location]
        print(f"The encoded text is {decrypted}")


caesar(text, shift, direction)
