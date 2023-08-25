"""
Miguel Angel Ruiz Martinez
951
19 de Agosto del 2023
Diseña una función desencripta(s, clave) que realice la función inversa a
la función anterior, es decir, reciba un string s y una clave y realice la
desencriptación del mensaje en el string devolviendo la cadena desencriptada."""

def desencripta(s, clave):
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    clave = {clave[i]: abecedario[i] for i in range(len(abecedario))}
    mensaje = ''

    for caracter in s:
        if caracter in clave:
            desencriptado = clave[caracter]
            mensaje += desencriptado
        else:
            mensaje += caracter
    return mensaje

clave = 'zyxwvutsrqponmlkjihgfedcba'
msg_encriptado1 = 'Angel'
mensaje_desencriptado1 = desencripta(msg_encriptado1, clave)
print(mensaje_desencriptado1)

msg_encriptado2 = 'Miguel'
mensaje_desencriptado2 = desencripta(msg_encriptado2, clave)
print(mensaje_desencriptado2)
