from ListaDoble import ListaDoble

l = ListaDoble(None, None, 0)
for i in range (1,21):
    if i%2 == 0:
        l.addLast(i)

temp = l.first()
while temp != None and temp.getNext() != None:
    print(temp.getData())
    temp = temp.getNext()
print(temp.getData())

print("\n")

##removidos los numero 1, 10 y 20
temp = l.first()
while temp!= None and temp.getData() != 10:
    temp = temp.getNext()
l.remove(temp)

temp = l.first()
while temp !=None and temp.getData() != 20:
    temp = temp.getNext()
l.remove(temp)

temp1 = l.first()
while temp1 != None and temp1.getNext() != None:
    print(temp1.getData())
    temp1 = temp1.getNext()



"""#Inciso a segunda parte
print("\n")

l1 = ListaDoble(None,None,0)
for i in range(1, 21):
    l1.addLast(i)
    
temp1 = l1.first()
while temp1 != None and temp1.getData() != 10:
    temp1 = temp1.getNext()
l1.remove(temp1), l1.removeFirst(), l1.removeLast()

temp1 = l1.first()
while temp1 != None and temp1.getNext() != None:
    print(temp1.getData())
    temp1 = temp1.getNext()"""
