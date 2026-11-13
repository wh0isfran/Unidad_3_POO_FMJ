class AdminRRHH: 
    def __init__(self, nombre: str, apellido_paterno: str, apellido_materno: str, id_admin: int, id_usuario: int | None = None):
        self.id_admin = id_admin
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno

    @property
    def id_usuario(self) -> int | None:
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor: int | None) -> None:
        if valor is not None:
            if type(valor) is not int or valor <= 0:
                raise ValueError(
                    "El ID de usuario debe ser un número entero positivo."
                )

        self._id_usuario = valor

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

    def __str__(self) -> str:
        id_str = self.id_admin if self.id_admin is not None else 'Sin asignar'
        return f"AdminRRHH [ID: {id_str}] | Nombre: {self.nombre} {self.apellido_paterno} {self.apellido_materno}"

    def __repr__(self) -> str:
        return f"AdminRRHH(id_admin={self.id_admin!r}, nombre={self.nombre!r}, apellido_paterno={self.apellido_paterno!r}, apellido_materno={self.apellido_materno!r})"