from datetime import datetime

class RegistroTiempo:
    def __init__(self, fecha: str, hora: str, descripcion: str, id_empleado: int, id_proyecto: int, id_registro: int = None):
        self.id_registro = id_registro
        self.fecha = fecha  
        self.hora = hora
        self.descripcion = descripcion
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto
        self.fecha_generacion = datetime.now().strftime("%Y-%m-%d") 
        self.periodo_mes = self.fecha[:7]  

    @property
    def fecha(self) -> str:
        return self._fecha

    @fecha.setter
    def fecha(self, value: str):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except (ValueError, TypeError):
            raise ValueError("La fecha debe tener formato YYYY-MM-DD.")
        
        self._fecha = value

    @property
    def fecha_generacion(self) -> str:
        return self._fecha_generacion
    
    @fecha_generacion.setter
    def fecha_generacion(self, value: str):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except (ValueError, TypeError):
            raise ValueError(
                "La fecha de generación debe tener formato YYYY-MM-DD."
            )

        self._fecha_generacion = value

    @property
    def periodo_mes(self) -> str:
        return self._periodo_mes
    
    @periodo_mes.setter
    def periodo_mes(self, value: str):
        from datetime import datetime

        try:
            datetime.strptime(value, "%Y-%m")
        except (ValueError, TypeError):
            raise ValueError("El período debe tener formato YYYY-MM.")

        self._periodo_mes = value

    @property
    def hora(self) -> str:
        return self._hora

    @hora.setter
    def hora(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 1:
            raise ValueError("La hora/formato de tiempo no es válido.")
        self._hora = valor.strip()

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("La descripción debe tener al menos 3 caracteres.")
        self._descripcion = valor.strip()

    def __str__(self) -> str:
        id_str = self.id_registro if self.id_registro is not None else 'Sin asignar'
        return f"RegistroTiempo [ID: {id_str}] | Fecha: {self.fecha} | Hora: {self.hora}"

    def __repr__(self) -> str:
        return f"RegistroTiempo(id_registro={self.id_registro}, fecha='{self.fecha}', hora='{self.hora}')"