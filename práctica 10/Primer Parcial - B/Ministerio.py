class Ministerio:
    def __init__(self, nombre, direccion, nro_empleados):
        self.nombre = nombre
        self.direccion = direccion
        self.nro_empleados = nro_empleados
        self.empleados = []

    def agregar_empleado(self, nombre, edad, sueldo):
        if len(self.empleados) < 4:
            self.empleados.append({"nombre": nombre, "edad": edad, "sueldo": sueldo})

    def eliminar_empleado_por_edad(self, edad_buscar):
        self.empleados = [e for e in self.empleados if e["edad"] != edad_buscar]

    def transferir_empleado(self, destino, nombre):
        for empleado in self.empleados:
            if empleado["nombre"] == nombre:
                destino.agregar_empleado(empleado["nombre"], empleado["edad"], empleado["sueldo"])
                self.empleados.remove(empleado)
                break

    def transferir_ultimo_empleado_a(self, destino):
        if self.empleados:
            ultimo = self.empleados.pop()
            destino.agregar_empleado(ultimo["nombre"], ultimo["edad"], ultimo["sueldo"])

    def mostrar_menor_edad(self):
        if not self.empleados:
            print("No hay empleados")
            return
        menor = min(self.empleados, key=lambda e: e["edad"])
        print(f"Empleado menor edad: {menor['nombre']}, Edad: {menor['edad']}")

    def mostrar_menor_sueldo(self):
        if not self.empleados:
            print("No hay empleados")
            return
        menor = min(self.empleados, key=lambda e: e["sueldo"])
        print(f"Empleado menor sueldo: {menor['nombre']}, Sueldo: {menor['sueldo']}")

ministerio_cultura = Ministerio("Ministerio de Cultura", "Calle 10", 4)
ministerio_deportes = Ministerio("Ministerio de Deportes", "Calle 12", 4)

ministerio_cultura.agregar_empleado("Pedro Rojas Luna", 35, 2500)
ministerio_cultura.agregar_empleado("Lucy Sosa Rios", 43, 3250)
ministerio_cultura.agregar_empleado("Ana Perez Rojas", 26, 2700)
ministerio_cultura.agregar_empleado("Saul Arce Calle", 29, 2500)

print("Ministerio de Cultura antes de eliminar empleados:")
ministerio_cultura.mostrar_menor_edad()
ministerio_cultura.mostrar_menor_sueldo()

ministerio_cultura.eliminar_empleado_por_edad(26)

print("\nMinisterio de Cultura después de eliminar empleados con edad 29:")
ministerio_cultura.mostrar_menor_edad()
ministerio_cultura.mostrar_menor_sueldo()

ministerio_cultura.transferir_empleado(ministerio_deportes, "Pedro Rojas Luna")

print("\nDespués de transferir a empleado:")
print("Ministerio de Cultura:")
ministerio_cultura.mostrar_menor_edad()
ministerio_cultura.mostrar_menor_sueldo()

print("Ministerio de Deportes:")
ministerio_deportes.mostrar_menor_edad()
ministerio_deportes.mostrar_menor_sueldo()