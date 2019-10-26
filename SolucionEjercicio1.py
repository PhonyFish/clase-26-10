# Nombre: SolucionEjercicio1.py
# Objetivo: Resolver ejercicio 1
# Autor: Luis Javier Ortiz Olguin
# Fecha: 26 de octubre de 2019

def main():
    sueldo = int(input("Ingrese sueldo del tabajador: "))
    
    if(sueldo < 1000):
        sueldo = sueldo * 1.15
    else:
        sueldo = sueldo * 1.12
    print("El nuevo sueldo del trabajador es: ", sueldo)

if __name__=="__main__":
    main()