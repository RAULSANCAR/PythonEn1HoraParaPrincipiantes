temperatura = float(input("Ingrese temperatura:"))
escala = input("¿Es Fahrenheit(f) ó es Celsius(c)?").lower()

if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print(celsius)
elif escala == "c":
    fahrenheit = temperatura * 1.8 + 32
    print(fahrenheit)
else:
    print("Escala incorrecta")
