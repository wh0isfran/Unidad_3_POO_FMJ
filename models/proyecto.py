class Proyecto:
    def __init__(self, nombre_proyecto: str, descripcion: str, fecha_inicio: str, id_proyecto: int | None = None):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio

    @property
    def nombre_proyecto(self) -> str:
        return self._nombre_proyecto

    @nombre_proyecto.setter
    def nombre_proyecto(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("El nombre del proyecto debe tener al menos 3 caracteres.")
        self._nombre_proyecto = valor.strip()

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 5:
            raise ValueError("La descripción debe tener al menos 5 caracteres.")
        self._descripcion = valor.strip()

    @property
    def fecha_inicio(self) -> str:
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 8:
            raise ValueError("La fecha de inicio debe ser válida.")
        self._fecha_inicio = valor.strip()

    def __str__(self) -> str:
        id_str = self.id_proyecto if self.id_proyecto is not None else 'Sin asignar'
        return f"Proyecto [ID: {id_str}] | Nombre: {self.nombre_proyecto} | Inicio: {self.fecha_inicio}"

    def __repr__(self) -> str:
        return f"Proyecto(id_proyecto={self.id_proyecto}, nombre_proyecto='{self.nombre_proyecto}', fecha_inicio='{self.fecha_inicio}')"