from cola_prioridad import ColaPrioridadPersonas
from persona import Persona

cola = ColaPrioridadPersonas()

while True:
    print("\nmenu:")
    print("1. agregar persona a la cola")
    print("2. listar personas en la cola")
    print("3. atender (eliminar de la cola)")
    print("4. salir")

    opcion = input("seleccione una opcion: ")

    if opcion == "1":
        nombre = input("nombre: ")
        apellido1 = input("primer apellido: ")
        apellido2 = input("segundo apellido: ")
        edad = int(input("edad: "))
        persona = Persona(nombre, apellido1, apellido2, edad)
        cola.encolar(persona)

    elif opcion == "2":
        cola.imprimir()

    elif opcion == "3":
        cola.desencolar()

    elif opcion == "4":
        print("saliendo...")
        break

    else:
        print("opcion invalida. intente de nuevo.")
