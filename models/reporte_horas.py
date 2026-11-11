class ReporteHoras:
    def __init__(
        self,
        id_empleado: int,
        id_proyecto: int,
        horas_trabajadas: float,
        fecha: str,
        periodo_mes: str,
        fecha_generacion: str,
        id_reporte: int = None
    ):
        self.id_reporte = id_reporte
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto
        self.horas_trabajadas = horas_trabajadas
        self.fecha = fecha
        self.periodo_mes = periodo_mes
        self.fecha_generacion = fecha_generacion

    @property
    def id_empleado(self) -> int:
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, value: int):
        if value <= 0:
            raise ValueError("El ID del empleado debe ser un valor positivo.")
        self._id_empleado = value

    @property
    def id_proyecto(self) -> int:
        return self._id_proyecto

    @id_proyecto.setter
    def id_proyecto(self, value: int):
        if value <= 0:
            raise ValueError("El ID del proyecto debe ser un valor positivo.")
        self._id_proyecto = value

    @property
    def horas_trabajadas(self) -> float:
        return self._horas_trabajadas

    @horas_trabajadas.setter
    def horas_trabajadas(self, value: float):
        if value < 0:
            raise ValueError("Las horas trabajadas no pueden ser negativas.")
        self._horas_trabajadas = float(value)

    @property
    def fecha(self) -> str:
        return self._fecha

    @fecha.setter
    def fecha(self, value: str):
        if not value.strip():
            raise ValueError("La fecha no puede estar vacía.")
        self._fecha = value

    @property
    def periodo_mes(self) -> str:
        return self._periodo_mes

    @periodo_mes.setter
    def periodo_mes(self, value: str):
        if not value.strip():
            raise ValueError("El periodo del mes no puede estar vacío.")
        self._periodo_mes = value

    @property
    def fecha_generacion(self) -> str:
        return self._fecha_generacion

    @fecha_generacion.setter
    def fecha_generacion(self, value: str):
        if not value.strip():
            raise ValueError("La fecha de generación no puede estar vacía.")
        self._fecha_generacion = value