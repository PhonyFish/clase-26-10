# Nombre: SolucionEjercicio2.py
# Objetivo: Resolver ejercicio 2
# Autor: Luis Javier Ortiz Olguin
# Fecha: 26 de octubre de 2019

def main():
    cat = int(input("Ingrese la categoría del trabajador"))
    sueldo = int(input("Ingrese sueldo del trabajador: "))
    
    if(cat == 1):
        sueldo = sueldo * 1.15
    elif(cat == 2):
        sueldo = sueldo * 1.10
    elif(cat == 3):
        sueldo = sueldo * 1.10
    elif(cat == 4):
        sueldo = sueldo * 1.10
    else:
        sueldo = -1
    
    if(sueldo == -1):
        print("Categoría invalida")
    else:
        print("El nuevo sueldo del trabajador es: ", sueldo)

if __name__=="__main__":
    main()