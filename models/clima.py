from datetime import datetime


class Clima:
    def __init__(self, ciudad: str, temperatura: float, humedad: float, viento: float, fecha_consulta: str, id_registro: int = None, id_clima: int = None):
        self.id_clima = id_clima
        self.id_registro = id_registro
        self.ciudad = ciudad
        self.temperatura = temperatura
        self.humedad = humedad
        self.viento = viento
        self.fecha_consulta = fecha_consulta

    @property
    def ciudad(self) -> str:
        return self._ciudad

    @ciudad.setter
    def ciudad(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("La ciudad debe tener al menos 3 caracteres.")
        self._ciudad = valor.strip()

    @property
    def temperatura(self) -> float:
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor: float) -> None:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("La temperatura debe ser un valor numérico.")
        if not -100 <= valor <= 60:
            raise ValueError("La temperatura está fuera del rango permitido.")
        self._temperatura = float(valor)

    @property
    def humedad(self) -> float:
        return self._humedad

    @humedad.setter
    def humedad(self, valor: float) -> None:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("La humedad debe ser un valor numérico.")
        if not 0 <= valor <= 100:
            raise ValueError("La humedad debe estar entre 0 y 100%.")
        self._humedad = float(valor)

    @property
    def viento(self) -> float:
        return self._viento

    @viento.setter
    def viento(self, valor: float) -> None:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("La velocidad del viento debe ser numérica.")
        if not 0 <= valor <= 500:
            raise ValueError("La velocidad del viento no es válida.")
        self._viento = float(valor)

    @property
    def fecha_consulta(self) -> str:
        return self._fecha_consulta

    @fecha_consulta.setter
    def fecha_consulta(self, valor: str) -> None:
        try:
            datetime.fromisoformat(valor)
        except (ValueError, TypeError):
            raise ValueError("La fecha de consulta debe tener formato ISO válido.")

        self._fecha_consulta = valor

    def __str__(self) -> str:
        id_str = self.id_clima if self.id_clima is not None else 'Sin asignar'
        return f"Clima [ID: {id_str}] | Ciudad: {self.ciudad} | Temperatura: {self.temperatura} °C | Humedad: {self.humedad}%"

    def __repr__(self) -> str:
        return f"Clima(id_clima={self.id_clima}, ciudad='{self.ciudad}', temperatura={self.temperatura}, fecha_consulta='{self.fecha_consulta}')"
