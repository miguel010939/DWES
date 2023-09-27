from random import sample
pos=["piedra", "papel", "tijera"]
score=0
# Sin los parentesis, estos operadores logicos me dan error por el orden de las operaciones: python trata de resolverlos antes de las comparaciones, que devolverian booleano, y los intenta aplicar a las strings
# Luego descubri que tambien existen los operadores equivalentes "and" y "or" que no dan estos problemas... Oooops
# Un poco raro que "&" y "and" tengan distinta prioridad operacional, pero bueno.. XD
# Resulta que no son equivalentes, Miguel: https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/ -> Operadores Bit a Bit
for i in range(5):
    user=input("\n¿Piedra, papel o tijera? ").lower()

    ai=sample(pos, 1)[0]
    if ai==user:
        print("Empate!")

    elif (user==pos[0]) & (ai==pos[2]) | (user==pos[1]) & (ai==pos[0]) | (user==pos[2]) & (ai==pos[1]):
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
