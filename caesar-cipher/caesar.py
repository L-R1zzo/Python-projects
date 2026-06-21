def caesar(text, shift, encrypt=True):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


while True:    
    what_to_do = input("Do you want to encrypt or decrypt?\n")    
    if what_to_do.lower() != "encrypt" and what_to_do.lower() != "decrypt":
        print("You can choose only between encrypt or decrypt")
    else:
        break

text = input("What is the message? --THE CIPHER ONLY WORKS WITH ALPHABET'S CHARACTERS--\n")

while True:
    try:
        shift_ = input("With which shift?\n")
        shift_ = int(shift_)
        if shift_ < 1 or shift_ > 25:
            print('Shift must be an integer between 1 and 25.\n')
        else:
            break
    except ValueError:
        print("Shift must be an integer!")


if what_to_do == "encrypt":
    print(encrypt(text, shift_)) 
else:
    print(decrypt(text, shift_))



    