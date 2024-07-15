import funcion as f

trabajadores = [
    "Juan Pérez", 
    "María García", 
    "Carlos López", 
    "Ana Martinez", 
    "Pedro Rodríguez", 
    "Laura Hernández", 
    "Miguel Sánchez", 
    "Isabel Gómez", 
    "Francisco Díaz", 
    "Elena Fernández"
]
sueldos = []
reporte = []

while True:
    print("MENU")
    print("1. Asignar Sueldos")
    print("2. Clasificar Sueldos")
    print("3. Ver Estadísticas")
    print("4. Reporte de Sueldos")
    print("5. Salir del Programa")
    opc = input("Ingrese opción (1 a 5): ")

    if opc == "1":
        f.asignar_sueldo(trabajadores, sueldos)
        print()
    elif opc == "2":
        f.clasificar_sueldos(sueldos)
    elif opc == "3":
        f.v_estadisticas(sueldos)
    elif opc == "4":
        f.reporte_s(sueldos)
    elif opc == "5":
        f.salir()
        break
    else: 
        print("Opción no valida, vuelve a intentar")
        continue