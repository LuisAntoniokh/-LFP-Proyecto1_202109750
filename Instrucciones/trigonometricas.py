import math
from Abstracto.abstract import Expression

class Trigonometricas(Expression):

    def __init__(self, left, tipo, fila, columna):
        self.left = left
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue=''

        if self.left != None:
            leftValue = self.left.operar(arbol)

        if self.tipo.operar(arbol) == 'Seno':
            resp = math.sin(leftValue)
            return math.degrees(resp)
        elif self.tipo.operar(arbol) == 'Coseno':
            resp = math.cos(leftValue)
            return math.degrees(resp)
        elif self.tipo.operar(arbol) == 'Tangente':
            resp = math.tan(leftValue)
            return math.degrees(resp)
        else:
            return None
    
    def getGraphLabel(self):
        return self.tipo + '\\n'+ str(self.operar(None))

    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()