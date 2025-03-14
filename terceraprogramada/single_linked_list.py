from nodo import nodo

class ListaEnlazadaOrdenada:
    def __init__(self):
        self.__list = None

    def insertar(self, persona):
        nuevo_nodo = nodo(persona)

        if self.__list is None or self.__list.getData().edad > persona.edad:
            nuevo_nodo.setNext(self.__list)
            self.__list = nuevo_nodo
            return

        current = self.__list
        while current.getNext() is not None and current.getNext().getData().edad < persona.edad:
            current = current.getNext()

        nuevo_nodo.setNext(current.getNext())
        current.setNext(nuevo_nodo)

    def imprimir(self):
        current = self.__list
        contador = 0
        while current:
            print(current.getData())
            current = current.getNext()
            contador += 1
        print(f"total de personas en la lista: {contador}")

    def eliminar_por_posicion(self, posicion):
        if self.__list is None:
            print("la lista esta vacia.")
            return

        if posicion == 0:
            self.__list = self.__list.getNext()
            return

        prev = None
        current = self.__list
        index = 0
        while current and index < posicion:
            prev = current
            current = current.getNext()
            index += 1

        if current is None:
            print(f"no existe la posicion {posicion}. la lista tiene {index} elementos.")
        else:
            prev.setNext(current.getNext())
            print(f"se elimino la persona en la posicion {posicion}.")
