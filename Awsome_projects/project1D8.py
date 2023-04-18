print('''      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|       ''')
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input('''Enter"encode" to encode and "decode " to decode \n ''' ).lower()
text = input("enter your text  \n").lower()
shift = int(input("enter the shift number \n "))


def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
       position =  alphabets.index(letter)
       new_position = ( position + shift_amount) % len(alphabets)
       new_letter = alphabets[new_position]
       cipher_text += new_letter
    print(f"the encodedd tex is{cipher_text}")   

encrypt(plain_text=text,shift_amount=shift)




