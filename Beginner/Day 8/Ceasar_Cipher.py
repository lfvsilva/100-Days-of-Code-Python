alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message, shift_number):
    encrypted_message = ""
    for i in message:
        if(i in alphabet):
            shifted_index = alphabet.index(i) + shift_number
            shifted_index %= len(alphabet)                
            encrypted_message += alphabet[shifted_index]
        else:
            encrypted_message += i
    return f"Here\'s the encoded result: {encrypted_message}" 

def decrypt(message, shift_number):
    decrypted_message = ""
    for i in message:
        if(i in alphabet):
            shifted_index = alphabet.index(i) - shift_number
            shifted_index %= len(alphabet)          
            decrypted_message += alphabet[shifted_index]
        else:
            decrypted_message += i
    return f"Here\'s the encoded result: {decrypted_message}"

def caesar(message, shift_number, encode_or_decode):
    output_message = ""
    if encode_or_decode == "decode":
        shift_number *= -1
    for i in message:
        if(i in alphabet):
            shifted_index = alphabet.index(i) + shift_number
            shifted_index %= len(alphabet)          
            output_message += alphabet[shifted_index]
        else:
            output_message += i
    return f"Here\'s the encoded result: {output_message}"

print('''
                                                                     
  ,ad8888ba,                                                         
 d8"'    `"8b                                                        
d8'                                                                  
88            ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
88            ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
Y8,           ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
 Y8a.    .a8P 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
  `"Y8888Y"'  `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          
                                                                     
                                                                                                                                     
  ,ad8888ba,  88             88                                 
 d8"'    `"8b ""             88                                 
d8'                          88                                 
88            88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
88            88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
Y8,           88 88       d8 88       88 8PP""""""" 88          
 Y8a.    .a8P 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
  `"Y8888Y"'  88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                 88                                             
                 88                                            

''')

try_again = True
while try_again:
    option = input("Type \'encode\' to encrypt, type \'decode\' to decrypt: \n").lower()
    message = input("Type your message: \n").lower()
    shift_number = int(input("Type the shift number: \n"))

    # if option == "encode":
    #     print(encrypt(message=message, shift_number=shift_number))
    #     try_option = input("Type \'yes\' if you want to go again. Otherwise type \'no\'.").lower()
    # elif option == "decode":
    #     print(decrypt(message=message, shift_number=shift_number))
    #     try_option = input("Type \'yes\' if you want to go again. Otherwise type \'no\'.").lower()
    # else:
    #     print("Type \'encode\' or \'decode\' \n")

    if option == "encode" or option == "decode":
        print(caesar(message=message, shift_number=shift_number, encode_or_decode=option))
        try_option = input("Type \'yes\' if you want to go again. Otherwise type \'no\'. \n").lower()
    else:
        print("Type \'encode\' or \'decode\' \n")
    if try_option != 'yes':
        break
