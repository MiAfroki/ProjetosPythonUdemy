massa = 79
altura = 1.70
imc = massa / (altura ** 2)

print(f"IMC: {imc}")

if imc < 19:
    print("Abaixo do peso.")
elif imc >= 19 and imc < 25: # elif -> else if -> senão se
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidade Grau I") # imc >= 30 and imc < 35
elif imc >= 35 and imc < 40:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")

print("Todos precisamos cuidar da saúde!")