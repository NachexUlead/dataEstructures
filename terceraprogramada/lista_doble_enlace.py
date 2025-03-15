from nodo_doble_enlace import NodoDoble

class ListaDobleOrdenada:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertar(self, persona):
        nuevo_nodo = NodoDoble(persona)

        if self.head is None or self.head.getData().edad > persona.edad:
            nuevo_nodo.setNext(self.head)
            if self.head:
                self.head.setPrev(nuevo_nodo)
            self.head = nuevo_nodo
            if self.tail is None:
                self.tail = nuevo_nodo
            print(f"{persona} fue agregado correctamente.")
            return

        current = self.head
        while current.getNext() and current.getNext().getData().edad < persona.edad:
            current = current.getNext()

        nuevo_nodo.setNext(current.getNext())
        nuevo_nodo.setPrev(current)
        if current.getNext():
            current.getNext().setPrev(nuevo_nodo)
        else:
            self.tail = nuevo_nodo
        current.setNext(nuevo_nodo)
        print(f"{persona} fue agregado correctamente.")

    def imprimir(self):
        if self.head is None:
            print("la lista esta vacía.")
            return

        current = self.head
        contador = 0
        while current:
            print(current.getData())
            current = current.getNext()
            contador += 1
        
        print(f"total de personas en la lista: {contador}")

    def eliminar_por_posicion(self, posicion):
        if self.head is None:
            print("la lista esta vacia.")
            return

        current = self.head
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
                self.head = current.getNext()
                if self.head:
                    self.head.setPrev(None)
                else:
                    self.tail = None

            print(f"se elimino: {current.getData()}")

    def buscar_por_edad(self, edad):
        if self.head is None:
            print("la lista esta vacia.")
            return

        if abs(self.head.getData().edad - edad) < abs(self.tail.getData().edad - edad):
            current = self.head
            direccion = "desde el inicio"
        else:
            current = self.tail
            direccion = "desde el final"

        encontrados = []
        while current:
            if current.getData().edad == edad:
                encontrados.append(current.getData())

            if direccion == "desde el inicio":
                current = current.getNext()
            else:
                current = current.getPrev()

        if encontrados:
            print(f"personas encontradas con la edad {edad}:")
            for persona in encontrados:
                print(persona)
        else:
            print(f"no se encontro ninguna persona con la edad {edad}.")
