from random import sample
pos=["piedra", "papel", "tijera"]
score=0
for i in range(5):
    user=input("\n¿Piedra, papel o tijera? ").lower()

    ai=sample(pos, 1)[0]
    if ai==user:
        print("Empate!")
    elif user==pos[0] & (ai==pos[2]) | (user==pos[1]) & (ai==pos[0]) | (user==pos[2]) & (ai==pos[1]):
        print("Victoria!")
        score+=1
    elif (user==pos[2]) & (ai==pos[0]) | (user==pos[0]) & (ai==pos[1]) | (user==pos[1]) & (ai==pos[2]):
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
