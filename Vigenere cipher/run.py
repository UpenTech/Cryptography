alpha_list = []


def alpha(var):
    for i in range(65, 91):
        if chr(i) not in var:
            var.append(chr(i))

alpha(alpha_list)

CIPHER_KEY = "WHITE"

def encrypt(text):
    en_text = ""

    for each in range(len(text)):
        tex = CIPHER_KEY[each % len(CIPHER_KEY)]
        num = alpha_list.index(tex)
        vig_list =  alpha_list[num:] + alpha_list[:num]
        
        cy_num = alpha_list.index(text[each].upper()) if text[each].upper() in alpha_list else 100

        if cy_num != 100:
            en_text += vig_list[cy_num]
        else:
            en_text += text[each]

    print(en_text)
    return en_text


def decrypt(text):
    de_text = ""

    for each in range(len(text)):
        tex = CIPHER_KEY[each % len(CIPHER_KEY)]
        num = alpha_list.index(tex)
        vig_list =  alpha_list[num:] + alpha_list[:num]
        
        cy_num = vig_list.index(text[each].upper()) if text[each].upper() in vig_list else 100

        if cy_num != 100:
            de_text += alpha_list[cy_num]
        else:
            de_text += text[each]

    print(de_text)

in_text = input("> ")
data = encrypt(in_text)
decrypt(data)