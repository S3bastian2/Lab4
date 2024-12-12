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

print("Se muestra la lista sin los valores 1, 10, 20")
print("\n")

#Eliminar valores 10, 20

temp2 = l1.First()
while temp2!= None and temp2.getData() != 10:
    temp2 = temp2.getNext()

temp = l1.First()
while temp!= None and temp.getData() != 8:
    temp = temp.getNext()
temp.setNext(temp2.getNext())
temp2.setNext(None)

temp3 = l1.First()
while temp3!= None and temp3.getData() != 20:
    temp3 = temp3.getNext()

temp4 = l1.First()
while temp4!= None and temp4.getData() != 18:
    temp4 = temp4.getNext()
temp4.setNext(temp3.getNext())
temp3.setNext(None)

temp1 = l1.First()
while temp1 != None and temp1.getNext() != None:
    print(temp1.getData())
    temp1 = temp1.getNext()

print(temp1.getData())