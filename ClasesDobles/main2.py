from Usuario import *
from ListaDoble import ListaDoble
from nodoDoble import nodoDoble
u1 = Usuario("David", 1, "Valledupar", 3134697894, "david@recocha.edu.co")
f1 = Fecha(13, 11, 2006)
d1 = Direccion("Kra 92", "74B-08", "Robledo", "Medellín", None, None)

u1.setFechaNacimiento(f1)
u1.setDir(d1)

u2 = Usuario("Carlos", 2, "Bogotá", 3123456789, "carlos@ejemplo.com")
f2 = Fecha(25, 5, 1992)
d2 = Direccion("Av. Chile", "21A-12", "Teusaquillo", "Bogotá", None, None)

u2.setFechaNacimiento(f2)
u2.setDir(d2)

u3 = Usuario("Ana", 3, "Medellín", 3145678901, "ana@correo.com")
f3 = Fecha(7, 8, 1990)
d3 = Direccion("Calle 45", "23B-09", "Laureles", "Medellín", None, None)

u3.setFechaNacimiento(f3)
u3.setDir(d3)

u4 = Usuario("Luis", 4, "Cali", 3156789012, "luis@ejemplo.com")
f4 = Fecha(10, 12, 1985)
d4 = Direccion("Calle 75", "14A-11", "San Fernando", "Cali", None, None)

u4.setFechaNacimiento(f4)
u4.setDir(d4)

u5 = Usuario("Laura", 5, "Barranquilla", 3178901234, "laura@correo.com")
f5 = Fecha(15, 3, 1995)
d5 = Direccion("Carrera 50", "9B-03", "Centro", "Barranquilla", None, None)

u5.setFechaNacimiento(f5)
u5.setDir(d5)

Usuarios = [u1,u2,u3,u4,u5]

l = ListaDoble(None, None, 0)
for i in range(len(Usuarios)):
    l.addLast(Usuarios[i])

temp = l.first()
while temp != None and temp != l.last():
    print(temp.getData())
    temp = temp.getNext()
print(l.last().getData())

#posteriormente

print("ingrese sus datos: ")
nombre = input("Ingrese su nombre: ")
id = input("Ingrese su id: ")
ciudadNacimiento = input("Ingrese su ciudad de nacimiento: ")
telefono =input("Ingrese su numero de telefono: ")
email = input("Ingrese su correo electronico: ")
usu1 = Usuario(nombre, id, ciudadNacimiento, telefono, email)
    
print("ingrese su fecha de nacimeinto")
dd = input("Ingrese su dia de nacimiento: ")
mm = input("Ingrese su mes de nacimiento: ")
aa = input("Ingrese el año de nacimiento: ")
f = Fecha(dd, mm, aa)
usu1.setFechaNacimiento(f)
print("ingrese su direccion: ")
calle = input("Ingrese su calle: ")
nomenclatura = input("Ingrese la nomenclatura (#): ")
barrio = input("Ingrese el barrio: ")
ciudad = input("Ingrese la ciudad: ")
edificio = input("Ingrese el edificio: ")
apto = input("Ingrese el numero de apartemento: \n")
d = Direccion(calle, nomenclatura, barrio, ciudad, edificio, apto)
usu1.setDir(d)
l.addFirst(usu1)

#usuario del final
print("ingrese sus datos otra vez: ")
nombre = input("Ingrese su nombre: ")
id = input("Ingrese su id: ")
ciudadNacimiento = input("Ingrese su ciudad de nacimiento: ")
telefono =input("Ingrese su numero de telefono: ")
email = input("Ingrese su correo electronico: ")
usu2 = Usuario(nombre, id, ciudadNacimiento, telefono, email)
    
print("ingrese su fecha de nacimeinto")
dd = input("Ingrese su dia de nacimiento: ")
mm = input("Ingrese su mes de nacimiento: ")
aa = input("Ingrese el año de nacimiento: ")
f = Fecha(dd, mm, aa)
usu2.setFechaNacimiento(f)
print("ingrese su direccion: ")
calle = input("Ingrese su calle: ")
nomenclatura = input("Ingrese la nomenclatura (#): ")
barrio = input("Ingrese el barrio: ")
ciudad = input("Ingrese la ciudad: ")
edificio = input("Ingrese el edificio: ")
apto = input("Ingrese el numero de apartemento: ")
d = Direccion(calle, nomenclatura, barrio, ciudad, edificio, apto)
usu2.setDir(d)
l.addLast(usu2)

temp = l.first()
while temp != None and temp != l.last():
    print(temp.getData())
    temp = temp.getNext()
print(l.last().getData())

#despues 3 Nodo
print("ingrese sus datos otra vez: ")
nombre = input("Ingrese su nombre: ")
id = input("Ingrese su id: ")
ciudadNacimiento = input("Ingrese su ciudad de nacimiento: ")
telefono =input("Ingrese su numero de telefono: ")
email = input("Ingrese su correo electronico: ")
usu3 = Usuario(nombre, id, ciudadNacimiento, telefono, email)
    
print("ingrese su fecha de nacimeinto")
dd = input("Ingrese su dia de nacimiento: ")
mm = input("Ingrese su mes de nacimiento: ")
aa = input("Ingrese el año de nacimiento: ")
f = Fecha(dd, mm, aa)
usu3.setFechaNacimiento(f)
print("ingrese su direccion: ")
calle = input("Ingrese su calle: ")
nomenclatura = input("Ingrese la nomenclatura (#): ")
barrio = input("Ingrese el barrio: ")
ciudad = input("Ingrese la ciudad: ")
edificio = input("Ingrese el edificio: ")
apto = input("Ingrese el numero de apartemento: ")
d = Direccion(calle, nomenclatura, barrio, ciudad, edificio, apto)
usu3.setDir(d)

temp = l.first()
for i in range (2):
    temp = temp.getNext()
l.addAfter(temp, usu3)

temp = l.first()
while temp != None and temp != l.last():
    print(temp.getData())
    temp = temp.getNext()
print(l.last().getData())