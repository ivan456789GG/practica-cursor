"""Calculadora interactiva: suma, resta, multiplicación y división."""


def pedir_numero(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.lower() == "salir":
            return None
        try:
            return float(texto)
        except ValueError:
            print("Eso no es un número válido. Inténtalo de nuevo o escribe 'salir'.")


print("Calculadora")
print("Operaciones: suma, resta, multiplicacion, division")
print("Escribe 'salir' en cualquier momento para terminar.\n")

while True:
    operacion = input("Operación (suma, resta, multiplicacion, division): ").strip().lower()

    if operacion == "salir":
        print("Hasta luego.")
        break

    if operacion not in ("suma", "resta", "multiplicacion", "multiplicación", "division", "división"):
        print("Operación no reconocida. Usa: suma, resta, multiplicacion o division.\n")
        continue

    a = pedir_numero("Primer número: ")
    if a is None:
        print("Hasta luego.")
        break

    b = pedir_numero("Segundo número: ")
    if b is None:
        print("Hasta luego.")
        break

    if operacion == "suma":
        print(f"Resultado: {a + b}\n")
    elif operacion == "resta":
        print(f"Resultado: {a - b}\n")
    elif operacion in ("multiplicacion", "multiplicación"):
        print(f"Resultado: {a * b}\n")
    elif operacion in ("division", "división"):
        if b == 0:
            print("Error: no se puede dividir entre cero.\n")
        else:
            print(f"Resultado: {a / b}\n")
