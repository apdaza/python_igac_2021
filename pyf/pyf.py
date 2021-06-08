from libreria_pyf import *

digitos = 2
intentos = 0
secreto = generar_secreto(digitos)
print(secreto)

msg = "intenta nuevamente"
while intentos < (digitos * 2):
    intentos += 1
    usuario = capturar_usuario(digitos)
    
    picas, fijas = comparar(secreto, usuario)

    print("picas: ", picas, "fijas: ", fijas)

    if fijas == digitos:
        msg = "Felicitaciones, ganaste en " + str(intentos) + " intentos"
        break

print(msg)
