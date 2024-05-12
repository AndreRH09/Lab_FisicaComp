FINAL_Gravedad = 9.8


def grafica():
  print("\nReferente a esta grafica, ingrese los datos")
  print("Considere que gravedad es 9.8 m/s^2")
  print("""\

         ........ 
       ............
      ..............
      |............|
      |  ........  |
      |            |
      |            |
      |            |
      |            |
      |            |
      |            |
  _________     _________
 |   m1    |   |   m2    |
 |_________|   |_________|
                      """)


def datos():
  masa1 = float(input("ingrese la masa del objeto 1 (en kg):"))
  #Verifica que ambas masas no negativas
  verificarNegativ(masa1)
  masa2 = float(input("ingrese la masa del objeto 2 (en kg):"))
  #Verifica que ambas masas no negativas
  verificarNegativ(masa2)

  aceleracion(masa1, masa2)


def verificarNegativ(masa):
  while (masa < 0):
    masa = float(input("El valor no puede ser negativo"))
  return masa


def aceleracion(masa1, masa2):
  acel = 0
  tens = 0
  if masa2 == masa1:
    acel = 0
    tens = masa1 * FINAL_Gravedad
    sentido = ""
  elif masa1 < masa2:
    acel = FINAL_Gravedad * (masa2 - masa1) / (masa2 + masa1)
    tens = tension(masa1, acel)
    sentido = "+j"

  else:
    acel = FINAL_Gravedad * (masa1 - masa2) / (masa2 + masa1)
    tens = tension(masa2, acel)
    sentido = "-j"

  print(f"La aceleracion del sistema es:\t {acel:.2f} m/s^2 , sentido: {sentido}")
  print(f"La Tension del sistema es:\t {tens:.2f} N")


def tension(masa, acel):
  return masa * (acel + FINAL_Gravedad)


if __name__ == "__main__":
  grafica()
  datos()
