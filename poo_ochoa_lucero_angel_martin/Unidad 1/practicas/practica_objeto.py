#Practica 2 clases, objetos, metodos y atributos

class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.__cuenta = None # Atributo privado

    def asignar_cuenta(self, cuenta):
          self.__cuenta = cuenta
          print(f"{self.nombre } ahora tienes una cuemta bancaria")

    def consultar_saldo(self):
        if self.__cuenta:
              print(f"El saldo de { self.nombre} es ") #saldo
        else:
              print(f"{self.nombre} no cuenta con cuenta bancaria")
                    

    def presentarse(self):
            print(f"hola, mi noombre es {self.nombre}, mi apellido es {self.apellido},y tengo {self.edad} años ")

    def cumplir_anios(self):
            self.edad +=1
            print(f"Esta persona cumplio: {self.edad} años")

class cuenta_bancaria:
    def __init__ (self,num_cuenta,saldo):
        self.num_cuenta = num_cuenta
        self.__saldo = saldo # Atributo privado
    
    def mostrar_saldo(self):
        return self.__saldo
    
    def depositar(self, cantidad):
        if cantidad >0:
            self.__saldo += cantidad
            print(f"se deposito la cantidad de ${self.cantidad}")
             
# Creacion del objeto o instancia de una clase:

estudiante1= Persona("Angel","Ochoa",19)
estudiante2= Persona("Yuri","Cervantes",19)

estudiante1.presentarse()
estudiante2.presentarse()

estudiante1.cumplir_anios()

# Ejercicio 1:

"""class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad



# Encapsulaminto
2"""