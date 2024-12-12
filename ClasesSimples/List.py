from Nodo import Nodo

class List():
    def __init__(self, head = Nodo, tail = Nodo, size = 0):
        self.__head = head
        self.__tail = tail
        self.__size = size
    
    def List(self):
        self.__init__()
    
    def isEmpty(self):
        if self.__size == 0:
            return True
        else:
            return False
    
    def setSize(self, s):
        self.__size = s
    
    def First(self):
        return self.__head
    
    def Last(self):
        return self.__tail
    
    def addFirst(self, e):
        n = Nodo(e)
        if self.isEmpty(n):
            self.__head = n
            self.__tail = n
        else:
            n.setNext(self.__head)
            self.__head = n
        self.__size += 1
    
    def addLast(self, e):
        n = Nodo(e)
        if self.isEmpty(n):
            self.__head = n
            self.__tail = n
        else:
            n.setNext(self.__tail)
            self.__tail = n
        self.__size += 1