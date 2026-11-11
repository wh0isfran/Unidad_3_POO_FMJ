class Departamento:
    def __init__(self, nombre: str, gerente: str, id_departamento: int | None = None):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.gerente = gerente

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("El nombre del departamento debe tener al menos 3 caracteres.")
        self._nombre = valor.strip().title()

    @property
    def gerente(self) -> str:
        return self._gerente

    @gerente.setter
    def gerente(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("El nombre del gerente debe tener al menos 3 caracteres.")
        self._gerente = valor.strip().title()

    def __str__(self) -> str:
        id_str = self.id_departamento if self.id_departamento is not None else 'Sin asignar'
        return f"Departamento [ID: {id_str}] | Nombre: {self.nombre} | Gerente: {self.gerente}"

    def __repr__(self) -> str:
        return f"Departamento(id_departamento={self.id_departamento}, nombre='{self.nombre}', gerente='{self.gerente}')"