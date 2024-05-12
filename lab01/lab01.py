def calc():
    print("\nIntroduzca qué desea calcular")
    print("1 : MRU")
    print("2 : MRUV")
    choice = int(input("Introduzca su opción: "))

    # OPCIÓN 1, CALCULADORA MRU
    if choice == 1:
        print("\nIntroduzca qué desea calcular")
        print("1 : Velocidad")
        print("2 : Distancia recorrida")
        print("3 : Tiempo")
        newChoice = int(input("Introduzca su opción: "))

        # Opción 1.1 Calcular Velocidad
        if newChoice == 1:
            print("\nIngrese los valores de:")
            distance = float(input("Distancia (en metros): "))
            time = float(input("Tiempo (en segundos): "))
            time = verificarValor(time)
            velocity = distance / time
            print(f"La velocidad es: {velocity} m/s")

        # Opción 1.2 Calcular Distancia
        elif newChoice == 2:
            print("\nIngrese los valores de:")
            velocity = float(input("Velocidad (en metros/segundos): "))
            time = float(input("Tiempo (en segundos): "))
            time = verificarValorNegativo(time)
            distance = velocity * time
            print(f"La distancia es: {distance} m")

        # Opción 1.3 Calcular Tiempo
        elif newChoice == 3:
            print("\nIngrese los valores de:")
            distance = float(input("Distancia (en metros): "))
            velocity = float(input("Velocidad (en metros/segundos): "))
            time = abs(distance / velocity)
            print(f"El tiempo  es: {time} s")
        else:
            print("Opción no válida, inicie otra vez el programa ")

    # OPCIÓN 2, CALCULADORA MRUV
    elif choice == 2:
        print("Introduzca qué desea calcular")
        print("1 : Distancia")
        print("2 : Velocidad final")
        newChoice = int(input("Introduzca su opción: "))

        # Calcula la distancia recorrida
        if newChoice == 1:
            print("\nIngrese los valores de:")
            veloInicial = float(input("Velocidad Inicial (en metros/segundos): "))
            aceleration = float(input("Aceleración (en m/s^2): "))
            time = float(input("Tiempo (en segundos): "))
            verificarValorNegativo(time)
            distance = (veloInicial * time) + (aceleration * (time**2)) / 2
            print(f"La distancia es: {distance} m")

        elif newChoice == 2:
            print("\nIngrese los valores de:")
            veloInicial = float(input("Velocidad Inicial (en metros/segundos): "))
            aceleration = float(input("Aceleración (en m/s^2): "))
            time = float(input("Tiempo (en segundos): "))
            verificarValorNegativo(time)
            veloFinal = (veloInicial * time) + (aceleration * time)
            print(f"La velocidad final es: {veloFinal} m/s")
        else:
            print("Opción no válida, inicie otra vez el programa ")
    else:
        print("Opción no válida, inicie otra vez el programa ")


def verificarValor(valor):
    while valor <= 0:
        valor = float(
            input("Este valor no puede ser negativo o cero, ingrese uno nuevo: "))
    return valor


def verificarValorNegativo(valor):
    while valor < 0:
        valor = float(
            input("Este valor no puede ser negativo, ingrese uno nuevo: "))
    return valor


def lab01():
    calc()


if __name__ == "__main__":
    lab01()
