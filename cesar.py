#Cesar Cipher
import string

#Define the alphabet to use
alphabet = len(string.ascii_lowercase)

#Funcion para rotar el caracter
def shift_by(char, shift):
# The isalpha() methods returns True if all characters in the string are alphabets, Otherwise, It returns False
    if char.isalpha():
        aux = ord(char) + shift
        z = 'z' if char.islower() else 'Z'
        if aux > ord(z):
            aux -= alphabet
        char = chr(aux)
        print char
    return char

def caesar(text, key):
    return ''.join(map(lambda char: shift_by(char, key), text))


caesar("TREATY IMPOSIBLE", 3)