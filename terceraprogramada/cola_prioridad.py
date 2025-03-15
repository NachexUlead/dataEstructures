from nodo import Nodo

class ColaPrioridadPersonas:
    def __init__(self):
        self.head = None

    def encolar(self, persona):
        nuevo_nodo = Nodo(persona)

        if self.head is None:
            self.head = nuevo_nodo
            print(f"{persona} fue agregado a la cola.")
            return

        if persona.edad >= 65:
            current = self.head
            prev = None
            while current and current.getData().edad >= 65:
                prev = current
                current = current.getNext()

            if prev is None:
                nuevo_nodo.setNext(self.head)
                self.head = nuevo_nodo
            else:
                nuevo_nodo.setNext(prev.getNext())
                prev.setNext(nuevo_nodo)
        else:
            current = self.head
            while current.getNext():
                current = current.getNext()
            current.setNext(nuevo_nodo)

        print(f"{persona} fue agregado a la cola con prioridad.")

    def desencolar(self):
        if self.head is None:
            print("la cola esta vacía. no hay nadie para eliminar.")
            return

        persona_eliminada = self.head.getData()
        self.head = self.head.getNext()
        print(f"se elimino: {persona_eliminada}")

    def imprimir(self):
        if self.head is None:
            print("la cola esta vacia.")
            return

        current = self.head
        print("estado actual de la cola:")
        while current:
            print(current.getData())
            current = current.getNext()
