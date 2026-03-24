import random

#words = [
#"python",
#"programa",
#"variable",
#"funcion",
#"bucle",
#"cadena",
#"entero",
#"lista",
#]

words = {"rock" : ["intoxicados",
                   "queen",
                   "evanescence",
                   "kiss",
                   "radiohead",
                   "nirvana",
                   "aerosmith"],
         "pop" : ["rupaul",
                  "abba",
                  "twice",
                  "miranda",
                  "madonna",
                  "shakira"],
         "musical" : ["heathers",
                      "cabaret",
                      "hairspray",
                      "hamilton",
                      "chicago",
                      "six",
                      "rent",
                      "beetlejuice",
                      "grease",
                      "matilda"]}

#word = random.choice(words)

print("¡Bienvenido al Ahorcado!")
print()
print("""
Géneros disponibles:
    Rock
    Pop
    Musical""")
print()
genre = input ("Elegí un género: ").lower()
while genre not in words:
    genre = input ("Género inexistente, por favor ingrese un género: ")
#word = random.choice(words[genre])

games = random.sample(words[genre],random.randint(1,len(words[genre])))
#genera una lista con palabras dentro de la categoria elegida. La cantidad de partidas a jugar se randomiza
#segun el total de elementos de la categoria.

while len(games) > 0:
    print(f"Partidas restantes: {len(games)}")
    guessed = []
    attempts = 6
    score = 0
    word = games[0]
    while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
     progress = ""
     for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
     print(progress)
# Verificar si el jugador ya adivinó la palabra completa
     if "_" not in progress:
        score += 6
        print("¡Ganaste!")
        break

     print(f"Intentos restantes: {attempts}")
     print(f"Letras usadas: {', '.join(guessed)}")

     letter = input("Ingresá una letra: ")

     if letter.isalpha():
        if letter in guessed:
         print("Ya usaste esa letra.")
        elif letter in word:
          guessed.append(letter)
          print("¡Bien! Esa letra está en la palabra.")
        else:
          guessed.append(letter)
          attempts -= 1
          score -= 1
          print("Esa letra no está en la palabra.")
     else:
       print("Entrada no válida. ")

     print()

    else:
     print(f"¡Perdiste! La palabra era: {word}")
     score = 0   #sobra aca pero se asegura por si se modifica lo demas

    print(f"Tu puntaje es: {score} ")
    del games[0]