from random import sample
pos=["piedra", "papel", "tijera"]
score=0
#Victoria user==ai+1 %3 --> pos.index(user)==(pos.index(ai)+1)%3
#Derrota user== ai+2 %3 --> pos.index(user)==(pos.index(ai)+2)%3
for i in range(5):
    user=input("\n¿Piedra, papel o tijera? ").lower()

    ai=sample(pos, 1)[0]
    if ai==user:
        print("Empate!")

    elif pos.index(user)==(pos.index(ai)+1)%3:
        print("Victoria!")
        score+=1
    elif pos.index(user)==(pos.index(ai)+2)%3:
        print("Derrota!")
        score-=1

    print("jugador ha elegido: ", user)
    print("computador ha elegido: ", ai)

print("\nPuntuación: ", score)
if score==0:
    print("Has empatado")
elif score<0:
    print("Has perdido")
elif score>0:
    print("Has ganado")
