from single_linked_list import ListaEnlazadaOrdenada
from persona import Persona

lista = ListaEnlazadaOrdenada()

while True:
    print("\n1. agregar persona")
    print("2. listar personas")
    print("3. borrar persona")
    print("4. salir")
    
    opcion = input("seleccione una opcion: ")

    if opcion == "1":
        nombre = input("nombre: ")
        apellido1 = input("primer apellido: ")
        apellido2 = input("segundo apellido: ")
        edad = int(input("edad: "))
        persona = Persona(nombre, apellido1, apellido2, edad)
        lista.insertar(persona)
    elif opcion == "2":
        lista.imprimir()
    elif opcion == "3":
        pos = int(input("posicion a borrar: "))
        lista.eliminar_por_posicion(pos)
    elif opcion == "4":
        print("saliendo...")
        break
    else:
        print("opcion invalida.")
