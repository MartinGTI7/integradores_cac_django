from abc import ABC, abstractmethod

##########################################CLASE PERSONA###########################################

class Persona():

    def __init__(self, nombre = None, edad = None, dni = None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return f"{self.__nombre}"
    
    @property
    def edad(self):
        return f"{self.__edad}"
    
    @property
    def dni(self):
        return f"{self.__dni}"
    
    @nombre.setter
    def nombre(self, nombre_ingresado):
        
        ok = True
        while (ok):
            if (str(nombre_ingresado).isalpha()):
                self.__nombre = nombre_ingresado
                ok = False
            else:
                print("El nombre ingresado no es válido... vuelva a intentarlo")
                nombre_ingresado = input("Ingrese el nombre de la persona:")


    @edad.setter
    def edad(self, edad_ingresada):
        
        ok = True
        while (ok):
            try:
                edad_ingresada = int(edad_ingresada)
            except:
                print("La edad ingresada debe ser un valor numerico entero... vuelva a intentarlo")
                edad_ingresada = input("Ingrese la edad de la persona:")
                continue

            if (edad_ingresada >= 0 and edad_ingresada < 130):
                self.__edad = edad_ingresada
                ok = False
            else:
                print("La edad ingresada no es válida... vuelva a intentarlo")
                edad_ingresada = input("Ingrese la edad de la persona:")


    @dni.setter
    def dni(self, dni_ingresado):
        
        ok = True
        while (ok):
            try:
                dni_ingresado = int(dni_ingresado)
            except:
                print("El DNI ingresado debe ser un valor numerico entero y sin puntos... vuelva a intentarlo")
                dni_ingresado = input("ingrese el dni de la persona:")
                continue

            if (dni_ingresado > 0 and dni_ingresado < 150000000):
                self.__dni = dni_ingresado
                ok = False
            else:
                print("El DNI ingresado no es válido... vuelva a intentarlo")
                dni_ingresado = input("ingrese el dni de la persona:")

    def mostrar(self):
        return f"El nombre de la persona es {self.__nombre}, su edad es {self.__edad} y su DNI es {self.__dni}"

    def es_mayor_de_edad(self):
        if (int(self.__edad) >= 18):
            return True
        else:
            return False

##########################################CLASE CUENTA###########################################

class Cuenta():

    def __init__(self, cantidad = None):
        self.__titular = Persona()
        self.__cantidad = cantidad
    
    @property
    def cantidad(self):
        return f"{self.__cantidad}"

    def mostrar(self):
        return f"El titular de la cuenta es {self.nombre}, la cantidad es ${self.__cantidad}"

    def ingresar(self, cantidad):
        if (self.__cantidad == None and cantidad >= 0):
            self.__cantidad = cantidad
        else:
            if (cantidad >= 0):
                self.__cantidad += cantidad

    def retirar(self, cantidad):
        if (self.__cantidad == None and cantidad >= 0):
            self.__cantidad = 0 - cantidad
        else:
            if (cantidad >= 0):
                self.__cantidad -= cantidad

#######################################CLASE CUENTA JOVEN#########################################

class CuentaJoven(Cuenta):
    
    def __init__(self, bonificacion = "25%", cantidad = None):
        super().__init__(cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return f"La bonificación es de {self.__bonificacion}"
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        if (self.edad >= 18 and self.edad < 25):
            return True
        else:
            return False
        
    def ingresar(self, cantidad):
        if (self.es_titular_valido()):
            super().ingresar(cantidad)
        else:
            print("Usted no puede ingresar dinero por no ser un usuario válido de Cuenta Joven")

    def retirar(self, cantidad):
        if (self.es_titular_valido()):
            super().retirar(cantidad)
        else:
            print("Usted no puede retirar dinero por no ser un usuario válido de Cuenta Joven")
    
    def mostrar(self):
        if (self.es_titular_valido()):
            return f"Cuenta Joven \n {super().mostrar()} \n Cuenta con una bonificacion del {self.__bonificacion}"        
        else:
            return f"No cumple con los requerimientos de edad para tener una Cuenta Joven"

######################################PROBANDO CLASE CUENTA#######################################

cuenta = CuentaJoven()

cuenta.nombre = "Martin"
cuenta.edad = 21
cuenta.dni = 34965896

print(f"Nombre: {cuenta.nombre}")
print(f"Edad: {cuenta.edad}")
print(f"DNI: {cuenta.dni}")
print(f"Es un titular válido: {cuenta.es_titular_valido()}")
cuenta.ingresar(3600.23)
cuenta.retirar(1000.10)
print(cuenta.mostrar())