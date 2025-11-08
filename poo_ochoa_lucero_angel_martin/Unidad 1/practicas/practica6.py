# ---------------------------------------------------
# Ejemplo de patrones de diseño: Factory y Observer
# Caso real: Sistema de notificaciones en una tienda online
# ---------------------------------------------------

# -------------------------------
# FACTORY PATTERN
# -------------------------------
# Permite crear objetos sin exponer la lógica de creación al cliente.
# En este caso, generamos diferentes tipos de notificaciones (Email, SMS, Push).

class Notificacion:
    def enviar(self, mensaje):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")


class NotificacionEmail(Notificacion):
    def enviar(self, mensaje):
        print(f"[EMAIL] Enviando correo: {mensaje}")


class NotificacionSMS(Notificacion):
    def enviar(self, mensaje):
        print(f"[SMS] Enviando mensaje de texto: {mensaje}")


class NotificacionPush(Notificacion):
    def enviar(self, mensaje):
        print(f"[PUSH] Enviando notificación push: {mensaje}")


# Factory que decide qué tipo de notificación crear
class NotificacionFactory:
    @staticmethod
    def crear_notificacion(tipo):
        if tipo == "email":
            return NotificacionEmail()
        elif tipo == "sms":
            return NotificacionSMS()
        elif tipo == "push":
            return NotificacionPush()
        else:
            raise ValueError("Tipo de notificación no soportado.")


# -------------------------------
# OBSERVER PATTERN
# -------------------------------
# Permite que varios objetos se "suscriban" a un evento y reciban notificaciones automáticamente.
# Caso: un carrito de compras que notifica a los observadores cuando se realiza una compra.

class Sujeto:
    def __init__(self):
        self._observadores = []

    def agregar(self, observador):
        self._observadores.append(observador)

    def eliminar(self, observador):
        self._observadores.remove(observador)

    def notificar(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)


class Observador:
    def actualizar(self, mensaje):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")


# Observadores concretos
class Inventario(Observador):
    def actualizar(self, mensaje):
        print(f"[INVENTARIO] Actualizando stock: {mensaje}")


class Finanzas(Observador):
    def actualizar(self, mensaje):
        print(f"[FINANZAS] Registrando venta: {mensaje}")


class Cliente(Observador):
    def actualizar(self, mensaje):
        print(f"[CLIENTE] Recibiendo confirmación: {mensaje}")


# -------------------------------
# SIMULACIÓN DE USO
# -------------------------------
if __name__ == "__main__":
    # FACTORY
    print("=== FACTORY ===")
    fabrica = NotificacionFactory()
    notificacion = fabrica.crear_notificacion("email")
    notificacion.enviar("Gracias por tu compra!")

    notificacion2 = fabrica.crear_notificacion("sms")
    notificacion2.enviar("Tu pedido ha sido enviado.")

    # OBSERVER
    print("\n=== OBSERVER ===")
    tienda = Sujeto()
    
    inventario = Inventario()
    finanzas = Finanzas()
    cliente = Cliente()

    tienda.agregar(inventario)
    tienda.agregar(finanzas)
    tienda.agregar(cliente)

    # Cuando ocurre una venta, se notifica a todos los observadores
    tienda.notificar("Compra realizada del producto X")
