import matplotlib.pyplot as plt
import sys


def on_key(event):
    if event.key == ' ':
        plt.close()
        sys.exit()


def verificarNegativ(valor):
    while (valor <= 0):
        valor = float(input("El valor no puede ser negativo o 0"))
    return valor


def fuerza_movil(masa, distancia, tiempo, velocidad_inicial, velocidad_final):
    aceleracion = (velocidad_final - velocidad_inicial) / tiempo
    fuerza = masa * aceleracion
    print(f"La fuerza que describe el móvil es: {fuerza} N")

    # Gráfica del proceso
    tiempo_total = tiempo
    tiempo_grafica = [0, tiempo, tiempo_total]
    velocidad_grafica = [velocidad_inicial, velocidad_final, velocidad_final]

    plt.plot(tiempo_grafica, velocidad_grafica)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')

    plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
    plt.suptitle(
        'Proceso de cambio de velocidad del móvil',
        fontsize=15,
    )

    plt.title(
        '(Presione espacio para terminar el programa)',
        fontsize=10,
        color='red',
    )

    plt.connect('key_press_event', on_key)

    plt.show()


masa = float(input("Ingrese la masa del móvil en kg: "))
distancia = float(input("Ingrese la distancia recorrida en metros: "))
tiempo = float(input("Ingrese el tiempo en segundos: "))
#verifica que el tiempo no sea negativo o 0
tiempo = verificarNegativ(tiempo)
velocidad_inicial = float(input("Ingrese la velocidad inicial en m/s: "))
velocidad_final = float(input("Ingrese la velocidad final en m/s: "))

fuerza_movil(masa, distancia, tiempo, velocidad_inicial, velocidad_final)
