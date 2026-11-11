class Empleado:
    def __init__(self, nombre: str, apellido_paterno: str, apellido_materno: str, edad: int, direccion: str, telefono: str, correo: str, id_empleado: int | None = None):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = valor.strip().title()

    @property
    def apellido_paterno(self) -> str:
        return self._apellido_paterno

    @apellido_paterno.setter
    def apellido_paterno(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise ValueError("El apellido paterno debe tener al menos 2 caracteres.")
        self._apellido_paterno = valor.strip().title()

    @property
    def apellido_materno(self) -> str:
        return self._apellido_materno

    @apellido_materno.setter
    def apellido_materno(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise ValueError("El apellido materno debe tener al menos 2 caracteres.")
        self._apellido_materno = valor.strip().title()

    @property
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, valor: int) -> None:
        if not isinstance(valor, int) or valor < 18 or valor > 120:
            raise ValueError("La edad debe ser un número entero entre 18 y 120.")
        self._edad = valor

    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 5:
            raise ValueError("La dirección debe tener al menos 5 caracteres.")
        self._direccion = valor.strip()

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 6:
            raise ValueError("El teléfono no es válido.")
        self._telefono = valor.strip()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str) -> None:
        if not isinstance(valor, str) or "@" not in valor:
            raise ValueError("El correo electrónico debe ser válido.")
        self._correo = valor.strip().lower()

    def __str__(self) -> str:
        id_str = self.id_empleado if self.id_empleado is not None else 'Sin asignar'
        return f"Empleado [ID: {id_str}] | Nombre: {self.nombre} {self.apellido_paterno} {self.apellido_materno} | Correo: {self.correo}"

    def __repr__(self) -> str:
        return f"Empleado(id_empleado={self.id_empleado}, nombre='{self.nombre}', apellido_paterno='{self.apellido_paterno}', correo='{self.correo}')"