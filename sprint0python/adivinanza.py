from random import sample
adivinanza1="Adivina, adivinanza...\n¿Qué tiene el rey en la panza?\n\na. Una cucharada de melaza\nb. De los sarracenos, una lanza\nc. Un cuenco y una taza\n"
adivinanza2="Adivina, adivinanza...\n¿Qué corre y no se cansa?\n\na. Eliud Kipchoge\nb. Un programa en Python\nc. La electricidad\n"
adivinanza3="Adivina, adivinanza...\n¿Qué vuelve cuando se lanza?\n\na. Un insulto\nb. Una amenaza\nc. Un boomerang\n"

# adivinanzas={adivinanza1:"b", adivinanza2:"a", adivinanza3:"c"}
adivinanzas=((adivinanza1, "b"), (adivinanza2, "a"), (adivinanza3, "c"))

puntuacion=0

for adivinanza in sample(adivinanzas, 2):
    print("\n"+adivinanza[0])
    x=input("Respuesta... ")
    if x==adivinanza[1]:
        print("Respuesta correcta!")
        puntuacion+=10
    else:
        print("Respuesta incorrecta!")
        print("La respuesta correcta era la ", adivinanza[1])
        puntuacion-=5

print("\nPuntuación total: "+str(puntuacion))



