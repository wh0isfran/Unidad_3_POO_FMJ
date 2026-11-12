class Departamento:
    def __init__(self, nombre: str, gerente_id: int | None, id_departamento: int | None = None):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.gerente_id = gerente_id

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("El nombre del departamento debe tener al menos 3 caracteres.")
        self._nombre = valor.strip().title()

    @property
    def gerente_id(self) -> int | None:
        return self._gerente_id

    @gerente_id.setter
    def gerente_id(self, valor: int | None) -> None:
        if valor is not None and (not isinstance(valor, int) or valor <= 0):
            raise ValueError("El ID del gerente debe ser un número entero válido.")
        self._gerente_id = valor

    def __str__(self) -> str:
        id_str = self.id_departamento if self.id_departamento is not None else 'Sin asignar'
        return f"Departamento [ID: {id_str}] | Nombre: {self.nombre} | ID del Gerente: {self._gerente_id}"

    def __repr__(self) -> str:
        return f"Departamento(id_departamento={self.id_departamento}, nombre='{self.nombre}', gerente_id={self._gerente_id})"