from lista_doble_enlace import lista_doble_enlace
from nodo_doble_enlace import nodo_doble

lista = lista_doble_enlace()

nodo1 = nodo_doble(99)
nodo2 = nodo_doble(21)
nodo3 = nodo_doble("hola")

lista.imprimir()
lista.insert(nodo1)
print("-----")
lista.insert(nodo2)
lista.imprimir()
print("++++++")
lista.insert(nodo3)
lista.imprimir()
print("======")
lista.delete(nodo2)
lista.imprimir()