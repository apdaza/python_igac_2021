f = open("notas.csv")
lineas = [x.strip("\n") for x in f.readlines()]
f.close()

matriz = [x.split(",") for x in lineas]
for m in matriz:
    m[2] = int(m[2]) * 0.35
    m[3] = int(m[3]) * 0.35
    m[4] = int(m[4]) * 0.30

f = open("definitivas.csv", "w")
for m in matriz:
    f.write(m[0]+",")
    f.write(m[1]+",")
    f.write(str(sum(m[2:])))
    f.write("\n")
f.close()

