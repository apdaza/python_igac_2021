import os

if os.path.exists("demo_crear.txt"):
    os.remove("demo_crear.txt")
else:
    print("No existe el archivo")

archivos = os.listdir("fuentes")

for a in archivos:
    #print(a)
    if os.path.exists("fuentes/" + str(a)) and not str(a)[:3] == "ren":
        os.rename("fuentes/" + str(a), "fuentes/renombrado_" + str(a))
    else:
        print("no puedo renombrar a: " + str(a))

for a in archivos:
    if os.path.exists("fuentes/" + str(a)):
        lista = str(a).split("_")
        os.rename("fuentes/" + str(a), "fuentes/" + lista[-1])
    else:
        print("no puedo renombrar a: " + str(a))

os.rmdir("borrable")
