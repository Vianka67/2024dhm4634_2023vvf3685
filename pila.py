class Nodo:
    def __init__(self, valor):
        self.valor =valor
        self.siguiente= None
class PilaEnlazada:
    def __init__(self):
        self.cima=None
        self.longitud=0