#  File: TestCipher.py

#  Description: The substitution ciphers replace individual characters in a string. 
# Transposition ciphers on the other hand scramble the characters in the string. 

#  Student's Name: Jadesola Jaiyesimi    

#  Student's UT EID: jaj3847
 
#  Partner's Name: Rylee Matousek

#  Partner's UT EID: rdm3335

#  Course Name: CS 313E 

#  Unique Number: 50295

#  Date Created: February 1st, 2020

#  Date Last Modified: February 7th, 2020

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(strng, key):
    strng = strng
    length_string=len(strng)
    key = key
    string_list=list(strng)

#create grid based on length of string and key
    matrix=[['-'] * length_string for i in range(key)]

#True means direction has hit the bottom and must reverse
#This code denotes which values in the 'matrix' will be used
#and zig zags through the fence in order to find them.
    direction=False
    y=0
    i=0
    for x in range(length_string):
        if y == (key-1):
            direction=True
        elif y == 0:
            direction=False
        matrix[y][x] = string_list[i]
        i+=1
        if direction is True:
            y-=1
        else:
            y+=1

#strip out empty characters in the matrix and return encoded string
    encode=[]
    for y in range(key):
        for x in range(length_string):
            if matrix[y][x] != '-':
                encode.append(matrix[y][x])
    return ''.join(encode)

def rail_fence_decode(strng, key):
    cipher = strng
    length_cipher = len(cipher)
    cipher_list = list(cipher)
    key = key

    # create grid based on length of string and key
    matrix = [['-'] * length_cipher for i in range(key)]


    #denotes which values in the fence/matrix are a part of the message
    #by zig zagging through the fence.
    direction=False
    y=0
    for x in range(length_cipher):
        if y == (key-1):
            direction=True
        elif y == 0:
            direction=False
        matrix[y][x] = '$'
        if direction is True:
            y-=1
        else:
            y+=1

    #replaces each denoted index with its corresponding letter of the cipher
    i=0
    for y in range(key):
        for x in range(length_cipher):
            if matrix[y][x] == '$':
                matrix[y][x]=cipher_list[i]
                i+=1

    direction=False
    decode=[]

    #reads the list diagonally again and decodes encrypted message
    for y in range(key):
        for x in range(length_cipher):
            if y == (key - 1):
                direction = True
            elif y == 0:
                direction = False
            decode.append(matrix[y][x])
            if direction is True:
                y -= 1
            else:
                y += 1

    return ''.join(decode[:length_cipher])




def filter_string(strng):
    strng = strng.lower()  # create lowercase string
    sfiltered = ''
    for i in strng:
        if ord(i) >= 97 and ord(i) <= 122:  # if character is not a lowercase letter ignore
            sfiltered += i

    return sfiltered  # placeholder for the actual return statement


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vignere algorithm. You may not use a 2-D list
def encode_character(p, s):
    x = ord(p) - ord('a')  # distance from a (0,0)
    y = ord(s) - ord('a')
    z = x + y
    if z > 26:  # loop around alphabet
        z = z - 26
    elif z == 26:  # value is a
        z = 0
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
        , 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encoded = alpha[z]
    return encoded  # placeholder for actual return statement


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the
#          Vignere algorithm. You may not use a 2-D list
def decode_character(p, s):
    x = ord(p) - ord('a')  # distance from a (0,0)
    y = ord(s) - ord('a')
    z = y - x
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
        , 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decoded = alpha[z]

    return decoded  # placeholder for actual return statement


#  Input: strng is a string of characters and pass is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vignere algorithm
def vignere_encode(strng, p):
    encoded_string = ''
    for i in range(len(strng)):
        x = (encode_character(p[i], strng[i]))
        encoded_string += x
    return encoded_string  # placeholder for the actual return statement


#  Input: strng is a string of characters and pass is a pass phrase
#  Output: function returns a single string that is decoded with
#          vignere algorithm
def vignere_decode(strng, p):
    decoded_string = ''
    for i in range(len(strng)):
        x = (decode_character(p[i], strng[i]))
        decoded_string += x
    return decoded_string  # placeholder for the actual return statement


def main():

    print('Rail Fence Cipher')
    print()

    plain_text = input('Enter Plain Text to be Encoded: ')  # prompt the user to enter plain text
    key_encode = int(input('Enter Key: '))  # prompt the user to enter the key
    print('Encoded Text:',rail_fence_encode(plain_text, key_encode))  # encrypt and print the plain text using rail fence cipher
    
    print()

    encoded_text = input('Enter Encoded Text to be Decoded: ')  # prompt the user to enter encoded text
    key_decode = int(input('Enter Key: '))  # prompt the user to enter the key
    print('Decoded Plain Text:',rail_fence_decode(encoded_text, key_decode))  # decrypt and print the encoded text using rail fence cipher
    print()

    print('Vigenere Cipher')
    print()

    text = input('Enter Plain Text to be Encoded: ')  # prompt the user to enter plain text
    plain_text = filter_string(text)  # filter string
    pass_phrase = input('Enter Pass Phrase (no spaces allowed): ')  # prompt the user to enter pass phrase
    pass_phrase = pass_phrase.lower()

    x = len(plain_text) - len(pass_phrase)

    for i in range(len(plain_text)):  # make pass phrase the same length as plain_text
        if x != 0:
            pass_phrase += pass_phrase[i]
            x -= 1

    print('Encoded Text:',vignere_encode(plain_text, pass_phrase))  # encrypt and print the plain text using vignere cipher
    print()
    vig_encoded_text = input('Enter Encoded Text to be Decoded: ')  # prompt the user to enter encoded text
    pass_phrase = input('Enter Pass Phrase (no spaces allowed): ')  # prompt the user to enter pass phrase
    pass_phrase = pass_phrase.lower()
    x = len(vig_encoded_text) - len(pass_phrase)
    for i in range(len(vig_encoded_text)):  # make pass phrase the same length as plain_text
        if x != 0:
            pass_phrase += pass_phrase[i]
            x -= 1
    print('Decoded Plain Text:',
          vignere_decode(vig_encoded_text, pass_phrase))  # decrypt and print the encoded text using vignere cipher
    print()

if __name__ == "__main__":
    main()
