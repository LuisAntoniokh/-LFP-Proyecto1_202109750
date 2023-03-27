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
        return "n"+str(self.correlativo)+str(self.cluster)
    
    def getGraphLabel(self):
        pass
    
    def getnodeDefinition(self, index, cluster):
        self.correlativo = index
        self.cluster = cluster
        return self.getGraphnode() + " [ shape=note, style=filled, fillcolor=\"#82589F\", label=\""+ self.getGraphLabel() + "\"]; \n"