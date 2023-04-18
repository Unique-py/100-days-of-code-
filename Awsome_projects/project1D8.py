alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print('''      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|       ''') 
direction = input('''Enter "encode" to encode and "decode" to decode\n''').lower()
text = input("Enter your text:\n").lower()
shift = int(input("Enter the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = (position + shift_amount) % len(alphabets)
        new_letter = alphabets[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}")


def decrypt(cipher_text ,shift_amount):
    plain_text=""
    for letter in cipher_text:
        position = alphabets.index(letter)
        new_position = (position - shift_amount) 
        plain_text += alphabets[new_position]
    print(f"THe decode word is {plain_text}")


if direction == "encode":
    encrypt(plain_text = text, shift_amount=shift)
elif direction =="decode":
    decrypt(cipher_text=text,shift_amount=shift)
