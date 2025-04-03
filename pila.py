class Nodo:
    def __init__(self, valor):
        self.valor =valor
        self.siguiente= None
class PilaEnlazada:
    def __init__(self):
        self.cima=None
        self.longitud=0
    def esta_vacia(self):
        return self.cima is None
    
    def apilar(self, valor):
        nuevo_nodo= nodo(valor)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo
        self.longitud += 1