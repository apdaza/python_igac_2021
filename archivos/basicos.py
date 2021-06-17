"""
open(nombre_archivo, modo)

open(nombre_archivo, "r") -> solo lectura -> error si no existe
open(nombre_archivo, "a") -> agregar contenido -> crea el archivo si no existe
open(nombre_archivo, "w") -> escritura -> crea el archivo si no existe
open(nombre_archivo, "x") -> crear archivo -> error si existe
"""

f = open("demo.txt", "r")
print(f.read())

f = open("/home/alejandro/Escritorio/curso python/ejercicios/archivos/demo.txt")
print(f.read())

# C:\\Users\Alejandro

f = open("fuentes/demo.txt")
print(f.read())

f = open("../demo.txt")
print(f.read())

f = open("demo_escritura.txt", "w")
f.write("Contenido para demo")
f.close()

f = open("demo_escritura.txt")
print(f.read())
f.close()

f = open("demo_escritura.txt", "a")
f.write("\tContenido para demo 2")
f.close()

f = open("demo_escritura.txt")
print(f.read())
f.close()

#f = open("demo_crear.txt", "x")
#f.close()

f = open("demo_crear.txt", "a")
f.write("agregando contenido")
f.close()

f = open("demo.txt")
print(f.readlines())



