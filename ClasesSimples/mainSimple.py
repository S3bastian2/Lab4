from List import List

#Agregamos los valores pares a la lista l1
l1 = List(None, None, 0)
for i in range (1,21):
    if i%2 == 0:
        l1.addLast(i)

#Imprimimos la lista l1
temp = l1.First()
while temp != None and temp.getNext() != None:
    print(temp.getData())
    temp = temp.getNext()
print(temp.getData())

#Eliminar valores 10, 20
temp = l1.First()
while temp!= None and temp.getData() != 10:
    temp = temp.getNext()
l1.remove(temp)

temp = l1.First()
while temp !=None and temp.getData() != 20:
    temp = temp.getNext()
l1.remove(temp)

temp1 = l1.First()
while temp1 != None and temp1.getNext() != None:
    print(temp1.getData())
    temp1 = temp1.getNext()