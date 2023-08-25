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
