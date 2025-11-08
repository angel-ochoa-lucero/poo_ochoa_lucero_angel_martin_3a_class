#practica 5. siglenton
#ejemplo de patron de diseño Singlenton - sistema de registro de logs.

class logger:
    #atributo para guardar la unica instancia
    _instancia= None
    #metodo _new_ contola la creacion del objeto antes de init y se asegura que solo exista una unica instancia de logger.
    def __new__(cls,*args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        cls._instancia.archivo = open("app.log", "a")
        return cls._instancia #devuelve siempre a la misma instancia.
    
    def registro (self, mensaje):
        self.archivo.write(mensaje + "\n")
        self.archivo.flush()#forza al archivo para que guardarse en el disco.

registro1 = logger() #creamos la unica instancia SIGLETON
registro2 = logger() #devuelve la misma instancia sin crear una nueva

registro1.registro("inicio de sesion en la aplicacion")
registro2.registro("el usuario se autentifico")

print(registro1 is registro2) #true o false
      #si me regreso true. es el mismo objeto en memoria