

class CambioMonedaView:
    @staticmethod
    def solicitar_moneda(mensaje: str) -> str:
        monedas = {
            "1": "USD",
            "2": "EUR",
            "3": "CLP",
            "4": "GBP",
            "5": "JPY"
        }

        while True:
            print("\n===== MONEDAS DISPONIBLES =====")
            print("1.- Dólar estadounidense (USD)")
            print("2.- Euro (EUR)")
            print("3.- Peso chileno (CLP)")
            print("4.- Libra esterlina (GBP)")
            print("5.- Yen japonés (JPY)")
            print("6.- Otra moneda (Formato ISO 4217)")
            opcion = input(mensaje).strip()
            
            if opcion in monedas:
                return monedas[opcion]
            
            if opcion == "6":
                codigo = input(
                    "Ingrese código ISO (ej. Real Brasileño = BRL): "
                ).strip().upper()
                if (
                    len(codigo) == 3
                    and codigo.isascii()
                    and codigo.isalpha()
                ):
                    return codigo
                
                print("Código inválido.")
                continue
            print("Opción inválida.")

    @staticmethod
    def mostrar_resultado(
        origen: str,
        destino: str,
        tasa: float,
        mensaje: str
    ) -> None:
        print("\n" + "=" * 50)
        print("             RESULTADO DE CONVERSIÓN")
        print("=" * 50)
        print(f"  Moneda de origen : {origen}")
        print(f"  Moneda de destino: {destino}")
        print("-" * 50)
        print(
            f"  Tipo de cambio   : "
            f"1 {origen} = {tasa:,.4f} {destino}"
        )
        print("-" * 50)
        print(f"  Estado: {mensaje}")
        print("=" * 50)

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"\n[CAMBIO MONEDA] {mensaje}")


