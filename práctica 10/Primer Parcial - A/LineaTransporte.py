class LineaTransporte:
    def __init__(self, color, tramo, nro_cabinas, nro_empleados):
        self.color = color
        self.tramo = tramo
        self.nro_cabinas = nro_cabinas
        self.nro_empleados = nro_empleados
        self.empleados = []

    def agregar_empleado(self, nombre, edad, sueldo):
        self.empleados.append({"nombre": nombre, "edad": edad, "sueldo": sueldo})

    def eliminar_empleado_por_apellido(self, apellido):
        self.empleados = [e for e in self.empleados if apellido not in e["nombre"]]

    def transferir_empleado(self, destino, nombre):
        for e in self.empleados:
            if e["nombre"] == nombre:
                destino.agregar_empleado(e["nombre"], e["edad"], e["sueldo"])
                self.empleados.remove(e)
                break

    def transferir_ultimo_empleado_a(self, destino):
        if self.empleados:
            e = self.empleados.pop()
            destino.agregar_empleado(e["nombre"], e["edad"], e["sueldo"])

    def __add__(self, otro):
        if isinstance(otro, tuple) and len(otro) == 2:
            nombre, origen = otro
            if isinstance(origen, LineaTransporte):
                for e in origen.empleados:
                    if e["nombre"] == nombre:
                        self.agregar_empleado(e["nombre"], e["edad"], e["sueldo"])
                        origen.empleados.remove(e)
                        break
        return self

    def mostrar_mayor_edad(self):
        pass

    def mostrar_mayor_sueldo(self):
        pass

class LineaTeleferico(LineaTransporte):
    def mostrar_mayor_edad(self):
        if not self.empleados:
            print("No hay empleados")
            return

        mayor = self.empleados[0]
        for empleado in self.empleados[1:]:
            if empleado["edad"] > mayor["edad"]:
                mayor = empleado

        print(f"Empleado mayor edad: {mayor['nombre']}, Edad: {mayor['edad']}")

    def mostrar_mayor_sueldo(self):
        if not self.empleados:
            print("No hay empleados")
            return

        mayor = self.empleados[0]
        for empleado in self.empleados[1:]:
            if empleado["sueldo"] > mayor["sueldo"]:
                mayor = empleado

        print(f"Empleado mayor sueldo: {mayor['nombre']}, Sueldo: {mayor['sueldo']}")

linea1 = LineaTeleferico("Rojo", "Estación Central, Estación Cementerio, Estación 16 de Julio", 20, 3)
datos_linea2 = ("Verde", "Libertador, Alto Obrajes, Obrajes e Irpavi", 35, 8)
linea2 = LineaTeleferico(*datos_linea2)

linea1.agregar_empleado("Pedro Rojas Luna", 35, 2500)
linea1.agregar_empleado("Lucy Sosa Rios", 43, 3250)
linea1.agregar_empleado("Ana Perez Rojas", 26, 2700)
linea1.agregar_empleado("Saul Arce Calle", 29, 2500)

print("Línea 1:")
linea1.mostrar_mayor_edad()
linea1.mostrar_mayor_sueldo()

linea1.eliminar_empleado_por_apellido("Rojas")
print("\nLínea 1 después de eliminar apellido 'Rojas':")
linea1.mostrar_mayor_edad()

linea2 + ("Lucy Sosa Rios", linea1)

print("Línea 1:")
linea1.mostrar_mayor_edad()
print("Línea 2:")
linea2.mostrar_mayor_edad()