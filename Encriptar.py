"""
Miguel Angel Ruiz Martinez
951
19 de Agosto del 2023
Diseñe una función encripta(s, clave), que reciba un string s con un mensaje
y un string con una clave de codificación, y retorne el mensaje codificado según
la clave leída. Los signos de puntuación y dígitos que aparecen en el mensaje deben
conservarse sin cambios. La clave consiste en una sucesión de las 26 letras minúsculas
del alfabeto, las cuales se hacen corresponder con el alfabeto básico (a...z, sin
la ñ o vocales acentuadas) de 26 letras. La primera letra de la clave se relaciona
con la letra 'a', la segunda con la letra 'b', etc. """

abecedario = 'abcdefghijklmnopqrstuvwxyz'
clave = "zyxwvutsrqponmlkjihgfedcba"

mensaje = "Angel Ruiz"
msg_clave = ''

for i in mensaje:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        mayuscula = i >= 'A' and i <= 'Z'
        codigo = clave[ord(i) - ord('A' if mayuscula else 'a')]

        if mayuscula:
            codigo = chr(ord(codigo))

        msg_clave += codigo
    else:
        msg_clave += i

print(msg_clave)