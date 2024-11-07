import random

def generar_numeros_aleatorios():
    return random.sample(range(1, 51), 5)

def obtener_numeros_usuario():
    numeros_usuario = []
    print("Introduce tus 5 números entre 1 y 50:")
    while len(numeros_usuario) < 5:
        try:
            numero = int(input(f"Número {len(numeros_usuario) + 1}: "))
            if numero < 1 or numero > 50:
                print("El número debe estar entre 1 y 50.")
            elif numero in numeros_usuario:
                print("Ya has elegido este número, intenta otro.")
            else:
                numeros_usuario.append(numero)
        except ValueError:
            print("Por favor, introduce un número válido.")
    return numeros_usuario

def verificar_ganador(numeros_usuario, numeros_sorteo):
    return set(numeros_usuario) == set(numeros_sorteo)

def main():
    numeros_sorteo = generar_numeros_aleatorios()
    print("\nBienvenido al simulador de lotería")
    
    numeros_usuario = obtener_numeros_usuario()
    print("\nNúmeros sorteados:", numeros_sorteo)
    print("Tus números:", numeros_usuario)
    
    if verificar_ganador(numeros_usuario, numeros_sorteo):
        print("\n¡Felicidades! Has ganado la lotería.")
    else:
        print("\nNo has ganado. ¡Intenta de nuevo!")

if __name__ == "__main__":
    main()
