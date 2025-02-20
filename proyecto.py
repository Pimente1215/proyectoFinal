

def numeroDeVocales(palabra):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    número = sum(1 for letra in palabra if letra in vocales)
    return número


def numeroDeConsonantes(palabra):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    numero = sum(1 for letra in palabra if letra.isalpha() and letra not in vocales)
    return numero


def numeroDePalabras(oracion):
    return len(oracion.split())


def main():
    total_vocales = 0
    total_consonantes = 0
    total_palabras = 0

    while True:
        print("\n--- Menú ---")
        print("1. Contar vocales en una palabra")
        print("2. Contar consonantes en una palabra")
        print("3. Contar palabras en una oración")
        print("4. Ver estadísticas acumuladas")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            palabra = input("Ingrese una palabra para contar sus vocales: ")
            vocales = numeroDeVocales(palabra)
            total_vocales += vocales
            print(f"La palabra '{palabra}' tiene {vocales} vocales.")
        
        elif opcion == '2':
            palabra = input("Ingrese una palabra para contar sus consonantes: ")
            consonantes = numeroDeConsonantes(palabra)
            total_consonantes += consonantes
            print(f"La palabra '{palabra}' tiene {consonantes} consonantes.")
        
        elif opcion == '3':
            oracion = input("Ingrese una oración para contar sus palabras: ")
            palabras = numeroDePalabras(oracion)
            total_palabras += palabras
            print(f"La oración tiene {palabras} palabras.")
        
        elif opcion == '4':
            print("\n--- Estadísticas acumuladas ---")
            print(f"Total de vocales: {total_vocales}")
            print(f"Total de consonantes: {total_consonantes}")
            print(f"Total de palabras: {total_palabras}")
        
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")

if __name__ == "__main__":
    main()
