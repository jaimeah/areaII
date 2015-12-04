from random import randint
adivinanza = randint(1,5)
print(adivinanza)

if adivinanza==1:
    print("Si")
if adivinanza==2:
    print("No")
if adivinanza==3:
    print("Tal vez")
if adivinanza==4:
    print("Pregunta de Nuevo")
if adivinanza==5:
    print("Exactamente")
