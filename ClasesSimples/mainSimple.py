from List import List

l1 = List(None, None, 0)
for i in range (1,21):
    if i%2 == 0:
        l1.addLast(i)

print(l1.__size)