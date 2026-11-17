from models.registro_tiempo import RegistroTiempo
from models.registro_tiempo_dao import RegistroTiempoDAO
from services.clima_service import ClimaService
from views.registro_tiempo_view import RegistroTiempoView


class RegistroTiempoController:
    def __init__(self):
        self.view = RegistroTiempoView()
        self.clima_service = ClimaService()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.agregar_registro()
            elif opcion == 2:
                self.editar_registro()
            elif opcion == 3:
                self.eliminar_registro()
            elif opcion == 4:
                self.imprimir_registro()
            elif opcion == 5:
                self.imprimir_registros()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo de la gestión de registros de tiempo.")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida.")

    def agregar_registro(self) -> None:
        datos = self.view.formulario_nuevo_registro()

        try:
            nuevo_registro = RegistroTiempo(
                fecha=datos["fecha"],
                hora=datos["hora"],
                descripcion=datos["descripcion"],
                id_empleado=datos["id_empleado"],
                id_proyecto=datos["id_proyecto"]
            )

            clima, mensaje = ClimaService.consultar_clima(
                datos["ciudad"]
            )

            if clima is None:
                self.view.mostrar_mensaje(mensaje)
                self.view.mostrar_mensaje(
                    "No se guardó el registro de tiempo."
                )
                return

            exito = RegistroTiempoDAO.crear_con_clima(
                nuevo_registro,
                clima
            )

            if exito:
                self.view.mostrar_mensaje(
                    f"Registro agregado con ID "
                    f"{nuevo_registro.id_registro}."
                )

                print("\n--- Clima registrado ---")
                print(f"Ciudad: {clima.ciudad}")
                print(f"Temperatura: {clima.temperatura} °C")
                print(f"Humedad: {clima.humedad} %")
                print(f"Viento: {clima.viento} km/h")
                print(f"Fecha de consulta: {clima.fecha_consulta}")

            else:
                self.view.mostrar_mensaje(
                    "Error al guardar en la base de datos."
                )

        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(
                f"Error en los datos ingresados: {e}"
            )


    def editar_registro(self) -> None:
        id_reg = self.view.solicitar_id()
        registro = RegistroTiempoDAO.obtener_por_id(id_reg)
        if not registro:
            self.view.mostrar_mensaje("Registro de tiempo no encontrado.")
            return

        datos_nuevos = self.view.formulario_editar_registro(registro)
        try:
            registro.fecha = datos_nuevos['fecha']
            registro.hora = datos_nuevos['hora']
            registro.descripcion = datos_nuevos['descripcion']
            registro.id_empleado = datos_nuevos['id_empleado']
            registro.id_proyecto = datos_nuevos['id_proyecto']

            exito = RegistroTiempoDAO.actualizar(registro)
            if exito:
                self.view.mostrar_mensaje("Registro de tiempo actualizado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al actualizar en la base de datos.")
        except (ValueError, TypeError) as e:
            self.view.mostrar_mensaje(f"Error en los datos modificados: {e}")

    def eliminar_registro(self) -> None:
        id_reg = self.view.solicitar_id()
        registro = RegistroTiempoDAO.obtener_por_id(id_reg)
        if not registro:
            self.view.mostrar_mensaje("Registro de tiempo no encontrado.")
            return

        if self.view.confirmar_eliminacion(str(id_reg)):
            exito = RegistroTiempoDAO.eliminar(id_reg)
            if exito:
                self.view.mostrar_mensaje("Registro de tiempo eliminado exitosamente.")
            else:
                self.view.mostrar_mensaje("Error al eliminar en la base de datos.")
        else:
            self.view.mostrar_mensaje("Operación cancelada.")

    def imprimir_registro(self) -> None:
        id_reg = self.view.solicitar_id()
        registro = RegistroTiempoDAO.obtener_por_id(id_reg)

        if registro:
            self.view.mostrar_registro(registro)

            clima = RegistroTiempoDAO.obtener_clima_por_registro(
                id_reg
            )

            self.view.mostrar_clima_registro(clima)

        else:
            self.view.mostrar_mensaje(
                "Registro de tiempo no encontrado."
            )

    def imprimir_registros(self) -> None:
        registros = RegistroTiempoDAO.obtener_todos()
        self.view.mostrar_lista_registros(registros)