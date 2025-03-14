import random

def bienvenido():
    nombre = input("Bienvenido al Juego del Ahocado. \nDime tu nombre: ")
    print(f"Bueno {nombre}, he pensado en una palabra secreta. ¡Tienes 8 intentos para adivinarla!")

def jugar_ahorcado():
    palabras1 = ["PYTHON", "OSOPOLAR", "CELULAR", "PSICOLOGIA", "AURICULARES", "LAPTOP"]
    palabra_secreta = random.choice(palabras1)  
    guiones = ["_"] * len(palabra_secreta)  
    intentos_maximos = 8  
    letras_adivinadas = []
    
    
    ahorcado = [
        """
        +---+
        |   |
            |
            |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========
        """
    ]
    
    print("La palabra secreta tiene", len(palabra_secreta), "letras")
    print(" ".join(guiones))  
    
    errores = 0  

    while intentos_maximos > 0 and "_" in guiones:  
        letra = input("\nIngresa una letra: ").upper()  

        if letra in letras_adivinadas:  
            print("Ya ingresaste esta letra. Intenta con otra.")
            continue  
        
        letras_adivinadas.append(letra)  
        
        if letra in palabra_secreta:  
            print("¡Bien! La letra está en la palabra.")
            for i in range(len(palabra_secreta)):  
                if palabra_secreta[i] == letra:
                    guiones[i] = letra
        else:
            print("La letra no está en la palabra.")
            intentos_maximos -= 1  
            errores += 1  
            print(ahorcado[min(errores, len(ahorcado) - 1)])  
        
        print("Palabra:", " ".join(guiones))  
        print(f"Intentos restantes: {intentos_maximos}")  

    if "_" not in guiones:
        print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
    else:
        print("\n¡Perdiste! La palabra era:", palabra_secreta)
        print(ahorcado[-1])  

while True:
    bienvenido() 
    jugar_ahorcado()  
    jugar_de_nuevo = input("\n¿Quieres jugar otra vez? (Si/No): ").strip().upper()
    if jugar_de_nuevo != "SI":
        print("¡Gracias por jugar! Nos vemos pronto. 👋")
        break
