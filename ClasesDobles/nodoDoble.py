class nodoDoble:
    def __init__(self, data, next, prev):
        self.__data = data
        self.__next = next
        self.__prev = prev
        
    def DoubleNode(self):
        self.__init__()
    
    def DoubleNode(self, d):
        self.__init__(d)
        
    def setData(self, d):
        self.__data = d
    
    def setNext(self, n):
        self.__next = n 
    
    def setPrev(self, p):
        self.__prev = p
        
    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next
    
    def getPrev(self):
        return self.__prev