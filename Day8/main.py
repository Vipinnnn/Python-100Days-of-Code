from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, key):

    if direction == "encode":
        cipherText = ""

        for i in range(len(text)):
            new_posi = (alphabet.index(text[i])+int(key)) % 26
            cipherText += alphabet[new_posi]
        print(f"Cipher text: {cipherText}")
    elif direction == "decode":
        plainText = ""
        for i in range(len(text)):
            new_posi = (alphabet.index(text[i])-int(key)) % 26
            plainText += alphabet[new_posi]
        print(f"Plain text: {plainText}")
    else:
        print("Not a valid input")


restart = True
while restart == True:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    key = int(input("Type the key:\n"))
    caesar(direction, text, key)
    ask = input("Do you want to continue, type yes or no:\n")
    if ask == "no":
        restart = False
