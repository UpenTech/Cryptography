import pyperclip as PC
import argparse

parser = argparse.ArgumentParser()
#Optional Flags for application
parser.add_argument("-e",  "--encrypt", help="Encrypts the argument with Vigenere's Cipher")
parser.add_argument("-d",  "--decrypt", help="Decrypts the cipher text passed as argument")
args = parser.parse_args()

alpha_list = []
CIPHER_KEY = "WHITE"

def alpha(var):
    """Appends letters of English Alphabet

    Args:
        var (list): Empty List 
    """
    for i in range(65, 91):
        #Avoid Duplicate
        if chr(i) not in var:
            var.append(chr(i))

def encrypt(text):
    """Encrypts the user's input with Vigenere's Cipher

    Args:
        text (string): text to be encrypted

    Returns:
        string : entrypted text
    """

    en_text = ""

    for each in range(len(text)):
        #Assign cypher letter to each plaintext letter
        tex = CIPHER_KEY[each % len(CIPHER_KEY)]
        num = alpha_list.index(tex)
        #Ceaser's List
        vig_list =  alpha_list[num:] + alpha_list[:num]
        #String validation for special characters
        cy_num = alpha_list.index(text[each].upper()) if text[each].upper() in alpha_list else 100

        if cy_num != 100:
            en_text += vig_list[cy_num]
        else:
            en_text += text[each]

    #PC.copy(en_text)
    return en_text

def decrypt(text):
    """Decrypts the cipher text to initial string

    Args:
        text (string): Cypher text
    """
    de_text = ""

    for each in range(len(text)):
        #Assign cypher letter to each encrypted letter
        tex = CIPHER_KEY[each % len(CIPHER_KEY)]
        num = alpha_list.index(tex)
        #Ceaser's List
        vig_list =  alpha_list[num:] + alpha_list[:num]
        #String validation for special characters
        cy_num = vig_list.index(text[each].upper()) if text[each].upper() in vig_list else 100

        if cy_num != 100:
            de_text += alpha_list[cy_num]
        else:
            de_text += text[each]

    print(de_text)




alpha(alpha_list)

if args.encrypt:                    #Encrypt argument == True
    in_text = args.encrypt
    # print(encrypt(in_text))
    PC.copy(encrypt(in_text))
elif args.decrypt:                  #Decrypt argument == True
    decrypt(args.decrypt)
else:                               #Argument == False
    in_text = input(">")
    print(encrypt(in_text))




