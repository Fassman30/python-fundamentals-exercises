import math
math.pi
#definimos una funcion que cacule el radio
def calcular_radio_circulo(radio):
    return math.pi *( (radio)**2)
print("********calculo de circulo******")
print("cual es el radio del circulo")
radio = int(input())

area=calcular_radio_circulo(radio)

print(f"El área del círculo es: {area}")    