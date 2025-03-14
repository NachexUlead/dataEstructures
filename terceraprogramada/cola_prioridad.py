from nodo import nodo

class ColaPrioridadPersonas:
    def __init__(self):
        self.__list = None

    def encolar(self, persona):
        nuevo_nodo = nodo(persona)

        if self.__list is None:
            self.__list = nuevo_nodo
            return

        if persona.edad >= 65:
            current = self.__list
            prev = None
            while current and current.getData().edad >= 65:
                prev = current
                current = current.getNext()

            if prev is None:
                nuevo_nodo.setNext(self.__list)
                self.__list = nuevo_nodo
            else:
                nuevo_nodo.setNext(prev.getNext())
                prev.setNext(nuevo_nodo)
        else:
            current = self.__list
            while current.getNext():
                current = current.getNext()
            current.setNext(nuevo_nodo)

    def desencolar(self):
        if self.__list:
            self.__list = self.__list.getNext()
