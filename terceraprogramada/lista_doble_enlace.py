from nodo_doble_enlace import nodo_doble

class ListaDobleOrdenada:
    def __init__(self):
        self.__list = None

    def insertar(self, persona):
        nuevo_nodo = nodo_doble(persona)

        if self.__list is None or self.__list.getData().edad > persona.edad:
            nuevo_nodo.setNext(self.__list)
            if self.__list:
                self.__list.setPrev(nuevo_nodo)
            self.__list = nuevo_nodo
            return

        current = self.__list
        while current.getNext() and current.getNext().getData().edad < persona.edad:
            current = current.getNext()

        nuevo_nodo.setNext(current.getNext())
        nuevo_nodo.setPrev(current)
        if current.getNext():
            current.getNext().setPrev(nuevo_nodo)
        current.setNext(nuevo_nodo)

    def imprimir(self):
        if self.__list is None:
            print("la lista esta vacia.")
            return

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

        current = self.__list
        index = 0

        while current and index < posicion:
            current = current.getNext()
            index += 1

        if current is None:
            print(f"no existe la posicion {posicion}. la lista tiene {index} elementos.")
        else:
            if current.getPrev():
                current.getPrev().setNext(current.getNext())
            if current.getNext():
                current.getNext().setPrev(current.getPrev())

            if posicion == 0:
                self.__list = current.getNext()

            print(f"se elimino la persona en la posicion {posicion}.")

    def buscar_por_edad(self, edad):
        if self.__list is None:
            print("la lista esta vacia.")
            return

        encontrados = []
        current = self.__list

        while current:
            if current.getData().edad == edad:
                encontrados.append(current.getData())
            current = current.getNext()

        if encontrados:
            print("personas encontradas con la edad", edad)
            for persona in encontrados:
                print(persona)
        else:
            print("no se encontro ninguna persona con esa edad.")
