import random
import csv

def asignar_sueldo(trabajadores, sueldos:list):
    for i in trabajadores:
        sueldo = random.randint(300000, 2500000)
        sueldos.append(f"{trabajadores}: {sueldo}")
        print(f"{i}: ${sueldo}")
            

def clasificar_sueldos(sueldos):
        print("Sueldos menores a $800.000 TOTAL: ")
        for i in sueldos:
            if i[1] <= 800000:
                print("Sueldos menores a $800.000 TOTAL: ")
                print("Nombre empleado \tSueldo")
                print(f"{i[0]} \t${i[1]}")
        print("Sueldos entre $800.000 y $2.000.000 TOTAL: ")
        for i in sueldos:
            if i[1] >= 800000 and i[1] <= 2000000:
                print("Nombre empleado \tSueldo")
                print(f"{i[0]} \t${i[1]}")
        print("Sueldos superiores a $2.000.000 TOTAL: ")
        for i in sueldos:
            if i[1] >= 2000000:
                print("Nombre empleado \tSueldo")
                print(f"{i[0]} \t${i[1]}")

def v_estadisticas(sueldos):
    while True:
        print("1. Sueldo más alto")
        print("2. Sueldo más bajo")
        print("3. Promedio de sueldos")
        print("4. Media geométrica")
        opc = input("ingrese una opción: ")

        if opc == "1":
            print("***Sueldo más Alto***")
            for i in sueldos:
                if i[1] >= sueldos:
                    print(f"Sueldo: {i[0]}")
        elif opc == "2":
            print("***Sueldo más Bajo***")
            for i in sueldos:
                if i[1] <= sueldos:
                    print(f"Sueldo: {i[1]}")
        elif opc == "3":
            print("***Promedio de Sueldos***")
            for i in sueldos:
                promedio = i[1] * len(i[1])
                print(f"Promedio: {promedio}")
        elif opc == "4":
            print()

def reporte_s(sueldos):
    for i in sueldos:

        with open("reporte.csv", "w") as file:
            escribir = csv.writer(file)
            escribir.writerow("Nombre empleado  Sueldo Base  Descuento Salud  Descuento AFP  Sueldo Líquido\n")
            escribir.writerows(sueldos)

def salir():
    print("""
        Finalizando programa...
        Desarrollado por Camilo Torres
        RUT 21.635.730-2
          """)
        


    
     

