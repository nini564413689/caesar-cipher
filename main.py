alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt (plain_text, shift_amount): # keep the name of parameter different from argument
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index (letter) #this function will only return the 1st index it found
        new_position = position + shift_amount
        if new_position > 25:
            new_position -= len (alphabet) #this if loop can be insteaded by just duplicate the alphabet list
        new_letter = alphabet [new_position]
        cipher_text += new_letter
    print (f"The encoded text is {cipher_text}")

def decrypt (text_need_decode, decode_key_number):
    decrypt_text = ""
    for letter in text_need_decode:
        position = alphabet.index (letter)
        decode_position = position - decode_key_number
        decode_letter = alphabet [decode_position]
        decrypt_text += decode_letter
    print (f"The decoded text is {decrypt_text}") 
        
if direction == "encode": 
    encrypt (text, shift)
elif direction == "decode":
    decrypt (text, shift)