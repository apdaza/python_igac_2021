# -*- coding: utf-8 -*-

import os

def cargar_porcentajes(archivo):
    f = open(archivo)
    lineas = [x.strip("\n") for x in f.readlines()]
    f.close()
    lineas = [(x.split(",")[0], int(x.split(",")[1])/100) for x in lineas]
    return lineas

def cargar(archivo):
    f = open(archivo)
    lineas = [x.strip("\n") for x in f.readlines()]
    f.close()
    return lineas

def calcular_notas(alumnos, porcentajes, materias, archivo):
    f = open(archivo)
    lineas = [x.strip("\n") for x in f.readlines()]
    f.close()
    notas = [[x.split(",")[0],
              x.split(",")[1].strip(" "),
              int(x.split(",")[2]),
              int(x.split(",")[3]),
              int(x.split(",")[4]), 0] for x in lineas]

    for a in alumnos:
        print("alumno: " + a)
        for m in materias:
            print("materia: " + m)
            for n in range(len(notas)):
                if notas[n][0] == a and  notas[n][1] == m:
                    notas[n][2] *= porcentajes[0][1]
                    notas[n][3] *= porcentajes[1][1]
                    notas[n][4] *= porcentajes[2][1]
                    notas[n][5] = int(notas[n][2] + notas[n][3] + notas[n][4])

    f = open("definitivas.txt", "w")
    for n in range(len(notas)):
        f.write(notas[n][0] + " en " + notas[n][1] + " tiene " + str(notas[n][5]))
        f.write("\n")
    f.close()

porcentajes = cargar_porcentajes("porcentajes.txt")
materias = cargar("materias.txt")
alumnos = cargar("alumnos.txt")

calcular_notas(alumnos, porcentajes, materias, "notas.txt")
