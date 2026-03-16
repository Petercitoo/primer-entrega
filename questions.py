import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

#Agregado de las categorias al juego

diccionario = {"Entorno" : [words[0],words[1]], 
"Datos" : [words[5],words[6],words[7]], 
"Logica": [words[2], words[3], words[4]]
}

categorias =  ", ".join(diccionario.keys())

cat = input(f'Seleccione una de las categorias existentes: {categorias} ')

word = random.choice(diccionario[cat]) 

guessed = []
attempts = 6
puntaje = 6
print('Bienvenido al Ahorcado!')
print()

while attempts > 0:
    # Mostrar progreso; letras adivinadas y guiones para las que faltan
    
    progress = ""

    for letter in word:
        if letter in guessed:
            progress += letter + ""
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palbra completa
    if "_" not in progress:
        print('¡Ganaste!')
        print(f'Tu puntaje es: {puntaje}')
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {','.join(guessed)}")

    letter = input("Ingresá una letra: ")

   #Funcion verificadora caracteres.
   
    if (len(letter) != 1) or not (letter.isalpha()):
        print('Entrada no válida')
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
    print()

else:
    print(f"Perdiste! La palabra era: {word}")
    puntaje = 0
    print(f'Tu puntaje es: {puntaje}')
