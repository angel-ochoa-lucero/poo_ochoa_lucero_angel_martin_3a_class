from datetime import date

class Libro:
    def __init__(self, titulo, autor, año, codigo, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.codigo = codigo
        self.disponible = disponible

    def mostrar_info(self):
        print(f"\n Libro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.año}")
        print(f"Código: {self.codigo}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")

    def marcar_como_prestado(self):
        self.disponible = False
        print(f"El libro '{self.titulo}' ha sido marcado como prestado.")

    def marcar_como_disponible(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido marcado como disponible.")

class Usuario:
    def __init__(self, nombre, id_usuario, correo):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.correo = correo
        self.prestamos = []

    def mostrar_info(self):
        print(f"\n Usuario: {self.nombre}")
        print(f"ID: {self.id_usuario}")
        print(f"Correo: {self.correo}")
        print(f"Préstamos activos: {len(self.prestamos)}")

    def solicitar_prestamo(self, libro):
        if libro.disponible:
            prestamo = Prestamo(libro, self)
            self.prestamos.append(prestamo)
            libro.marcar_como_prestado()
            print(f"{self.nombre} ha realizado un préstamo del libro '{libro.titulo}'.")
            return prestamo
        else:
            print(f"El libro '{libro.titulo}' no está disponible.")
            return None

class Estudiante(Usuario):
    def __init__(self, nombre, id_usuario, correo, carrera, semestre):
        super().__init__(nombre, id_usuario, correo)
        self.carrera = carrera
        self.semestre = semestre

    def mostrar_info(self):
        print(f"\n Estudiante: {self.nombre}")
        print(f"ID: {self.id_usuario}")
        print(f"Correo: {self.correo}")
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")
        print(f"Préstamos activos: {len(self.prestamos)}")

class Profesor(Usuario):
    def __init__(self, nombre, id_usuario, correo, departamento, tipo_contrato):
        super().__init__(nombre, id_usuario, correo)
        self.departamento = departamento
        self.tipo_contrato = tipo_contrato
    
    def mostrar_info(self):
        print(f"\n Profesor: {self.nombre}")
        print(f"ID: {self.id_usuario}")
        print(f"Correo: {self.correo}")
        print(f"Departamento: {self.departamento}")
        print(f"Tipo de contrato: {self.tipo_contrato}")
        print(f"Préstamos activos: {len(self.prestamos)}")


class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None

    def registrar_prestamo(self):
        print(f"\nPréstamo registrado:")
        print(f"Usuario: {self.usuario.nombre}")
        print(f"Libro: {self.libro.titulo}")
        print(f"Fecha de préstamo: {self.fecha_prestamo}")

    def devolver_libro(self):
        self.fecha_devolucion = date.today()
        self.libro.marcar_como_disponible()
        print(f" Libro '{self.libro.titulo}' devuelto el {self.fecha_devolucion} por {self.usuario.nombre}.")

if __name__ == "__main__":
    
    libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "L001")
    libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, "L002")

    usuario1 = Usuario("María López", 1001, "maria@example.com")
    estudiante1 = Estudiante("Juan Pérez", 2001, "juan@example.com", "Ingeniería", 4)
    profesor1 = Profesor("Dr. Gómez", 3001, "gomez@example.com", "Ciencias Sociales", "Tiempo Completo")

    usuarios = [usuario1, estudiante1, profesor1]
    for u in usuarios:
        u.mostrar_info()

    libro1.mostrar_info()
    libro2.mostrar_info()

    print("\n--- Simulación de préstamo ---")
    prestamo1 = estudiante1.solicitar_prestamo(libro1)
    if prestamo1:
        prestamo1.registrar_prestamo()

    libro1.mostrar_info()

    print("\n--- Devolución del libro ---")
    prestamo1.devolver_libro()
    libro1.mostrar_info()