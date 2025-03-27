# Ejercicio examen parcial 2 (puntos extra)
# Algoritmos y Programación
# Otoño 2019

# Encontrar el número de dígitos de un número que son divisores   
# de dicho número (valen dígitos repetidos).   

# Función (proceso)
def digitos_divisores(n):
    digits = [int(i) for i in str(n)]
    n_divs = 0
    for i in digits:
        if i != 0 and n % i == 0:
            n_divs += 1
    return n_divs

if __name__ == "__main__":
    # Entradas
    numero = int(input("Introduzca un entero: "))

    # Proceso
    # Definido en la función
    divisores = digitos_divisores(numero)

    # Salidas
    print("Cantidad de dígitos que son divisores:", divisores)