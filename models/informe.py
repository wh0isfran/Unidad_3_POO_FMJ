class Informe:
    def __init__(self, titulo: str, fecha: str, contenido: str, id_informe: int | None = None):
        self.id_informe = id_informe
        self.titulo = titulo
        self.fecha = fecha
        self.contenido = contenido

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("El título debe tener al menos 3 caracteres.")
        self._titulo = valor.strip()

    @property
    def fecha(self) -> str:
        return self._fecha

    @fecha.setter
    def fecha(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 6:
            raise ValueError("La fecha no es válida.")
        self._fecha = valor.strip()

    @property
    def contenido(self) -> str:
        return self._contenido

    @contenido.setter
    def contenido(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 5:
            raise ValueError("El contenido debe tener al menos 5 caracteres.")
        self._contenido = valor.strip()

    def __str__(self) -> str:
        id_str = self.id_informe if self.id_informe is not None else 'Sin asignar'
        return f"Informe [ID: {id_str}] | Título: {self.titulo} | Fecha: {self.fecha}"

    def __repr__(self) -> str:
        return f"Informe(id_informe={self.id_informe}, titulo='{self.titulo}', fecha='{self.fecha}')"