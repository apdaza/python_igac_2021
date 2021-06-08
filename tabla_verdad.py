valor_uno = True
valor_dos = False

# comportamiento del and

print(valor_uno, " and ", valor_uno, " = ", (valor_uno and valor_uno))
print(valor_uno, " and ", valor_dos, " = ", (valor_uno and valor_dos))
print(valor_dos, " and ", valor_uno, " = ", (valor_dos and valor_uno))
print(valor_dos, " and ", valor_dos, " = ", (valor_dos and valor_dos))
print()
# comportamiento del or
print(valor_uno, " or ", valor_uno, " = ", (valor_uno or valor_uno))
print(valor_uno, " or ", valor_dos, " = ", (valor_uno or valor_dos))
print(valor_dos, " or ", valor_uno, " = ", (valor_dos or valor_uno))
print(valor_dos, " or ", valor_dos, " = ", (valor_dos or valor_dos))
print()
# comportamiento del not
print("not ", valor_uno, " = ", (not valor_uno))
print("not ", valor_dos, " = ", (not valor_dos))
