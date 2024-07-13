import random

trabajadores = [
    "Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", 
    "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", 
    "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"
]
sueldos = []

def menu():
    print("Bienvenido al sistema de gestión de sueldos")
    print("1. Asignar Sueldos Aleatorios")
    print("2. Clasificar Sueldos")
    print("3. Ver Estadísticas")
    print("4. Reporte de Sueldos")
    print("5. Salir del programa")
    opcion = input("Ingrese una opción: ")
    return opcion

# opción 1
# Para la generación de estos sueldos debe crear una función 
# capaz de generar los 10 sueldos de forma aleatoria los que
# serán usados posteriormente para la ejecución del programa.

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados...")
    
    
    
# opción 2   
# Deberá desarrollar una función que permita mostrar 
# la lista de empleados con su sueldo y su respectiva 
# clasificación según el siguiente esquema

def clasificar_sueldos():
    global sueldos
    sueldos.sort(reverse=True)
    print("Sueldos clasificados de mayor a menor:")
    for idx, sueldo in enumerate(sueldos, start=1):
        print(f"{idx}. ${sueldo}")
        
        
        
# opcion 3 
# Crear una función que permita mostrar por pantalla los siguientes datos
# con respecto a los sueldos:
# Sueldo más alto
# Sueldo más bajo
# Promedio de sueldos
# Media geométrica
def ver_estadisticas():
    global sueldos
    if not sueldos:
        print("Primero debe asignar sueldos aleatorios.")
        return
    
    sueldo_mas_alto = max(sueldos)
    sueldo_mas_bajo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)

    media_geom = 1
    for sueldo in sueldos:
        media_geom *= sueldo
    media_geom **= (1 / len(sueldos))
    
    print(f"Sueldo mas alto: ${sueldo_mas_alto}")
    print(f"Sueldo mas bajo: ${sueldo_mas_bajo}")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
    print(f"Media geometrica de sueldos: ${media_geom:.2f}")
    
    
    
# opcion 4: 
# La aplicación deberá poseer una función para mostrar el detalle de los sueldos
# de los trabajadores, según la siguiente regla de negocio:
# Descuento salud 7%
# Descuento AFP 12%
# Sueldo líquido calculado en base al sueldo base menos el descuento en salud y menos el descuento afp.

def reporte_sueldos():
    global sueldos
    if not sueldos:
        print("Primero debe asignar sueldos aleatorios.")
        return
    
    print("Reporte de Sueldos:")
    print("{:<20} {:<15} {:<15}".format("Empleado", "Sueldo Bruto", "Sueldo Líquido"))
    for idx, (empleado, sueldo) in enumerate(zip(trabajadores, sueldos), start=1):
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        print("{:<20} ${:<15,.2f} ${:<15,.2f}".format(empleado, sueldo, sueldo_liquido))
        
        
        
#La aplicación deberá finalizar
# para salir el programa mostrando un mensaje con sus datos
def salir_programa():
    print("Finalizando programa...")
    print("Desarrollado por Emilio Jaramillo")
    print("Rut 19.239.196-2")
    
    

def main():
    while True:
        opcion = menu()
        
        if opcion == '1':
            asignar_sueldos_aleatorios()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            salir_programa()
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()