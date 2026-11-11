def leer_numero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def confirmar(mensaje: str) -> bool:
    while True:
        resp = input(f"{mensaje} (si/no): ").strip().lower()
        if resp in ("si", "no"):
            return resp == "si"
        print("Respuesta no válida. Por favor, ingrese 'si' o 'no'.")

def leer_texto(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error: El campo no puede estar vacío.")