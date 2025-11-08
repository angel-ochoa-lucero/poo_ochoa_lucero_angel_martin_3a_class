# practica 4 herencia

class ticket:
    def _init_(self, id, tipo, prioridad):
        self.id= id
        self.tipo=tipo
        self.prioridad=prioridad
        self.estado="pendiente"
        
ticket1= ticket (1, "prueba", "baja" )
ticket2=ticket (2, "software", "alto")

#clase padre
class empleado:
    def _unit_(self, nombre):
        self.nombre=nombre
    def trabajar_ticket(self, ticket):
        print (f"El empleado {self.nombre} revisa el ticket {ticket.id}")
        
class desarrollador(empleado):
    def trabajar_ticket(self, ticket):
        if ticket.tipo =="software":
            ticket.estado = "resuelto"
            print (f"el ticket {ticket.id} fue resuelto por {self.nombre} ")
        else:
            ticket.estado = "no resuelto"
            print (f"el ticket {ticket.id} fue no ha sido resuelto por {self.nombre} ")
        
class tester(empleado):
    def trabajar_ticket(self, ticket):
        if ticket.tipo =="prueba":
            ticket.estado = "resuelto"
            print (f"el ticket {ticket.id} fue resuelto por {self.nombre} ")
        else:
            ticket.estado = "no resuelto"
            print (f"el ticket {ticket.id} fue no ha sido resuelto por {self.nombre} ")


class projectmanager(empleado):
    def asingar_ticket(self, ticket, empleado):
        print(f"{self.nombre} asigno el ticket {self.ticket} al empleado {empleado.nombre}")
        empleado.trabajar_en_ticket(ticket)
        
# crear tickets y empleados (instancias de objetos)
ticket1=ticket(1, "software", "alta")
ticket2=ticket(2, "prueba", "baja")

developer1= desarrollador("Carlitos")
tester1= tester("Juanillo")
pm=projectmanager("Marianita")

pm.asignar_ticket(ticket2,developer1)
pm.asingar_ticket(ticket1,tester1)

#