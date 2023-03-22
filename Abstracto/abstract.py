from abc import ABC, abstractmethod

class Expression(ABC):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        
    @abstractmethod
    def operar(self, arbol):
        pass

    @abstractmethod
    def getFila(self):
        return self.fila

    @abstractmethod
    def getColumna(self):
        return self.columna
    
    def getGraphnode(self):
        return 'n'+str(self.correlativo)
    
    def getGraphLabel(self):
        pass
    
    def getnodeDefinition(self, index):
        self.correlativo = index
        return self.getGraphnode(index) + ' [ label=\''+ self.getGraphLabel() + '\']; \n'