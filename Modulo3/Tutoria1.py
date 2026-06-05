#arquitectura SaaS
#separar el proyecto por resposabilidades, dominio funcional, dominio de negocio, dominio de infraestructura

#capas tecnicas = codigo no se vuelva caotico

#organizacion del sistema por las areas del negocio, por ejemplo: ventas, compras, recursos humanos, etc

## POO

## clases      ====  > molde, plantilla, plano, etc
## atributos   ====  > caracteristicas, propiedades, etc
## metodos     ====  > acciones, comportamientos, etc

## OBJETOS     ====  > instancias de una clase, es decir, objetos concretos que se crean a partir de la clase

## LOS 4 PILARES DEL POO

### HERENCIAS  === > es el proceso de crear una nueva clase a partir de una clase existente,
# clase padre, o principal o superclase, clase base
vehiculo = {
    "llantas"
    "puertas"
    "ventanas"
}
{encender, apagar, acelerar}

#clase hija, o secundaria o subclase, clase derivada
automovil = {
    "marca"
    "modelo"
    "color"
}
{encender, apagar, acelerar, tocar bocina, abrir puertas, cerrar puertas}

#clase hija, o secundaria o subclase, clase derivada
deportivo = {
    "placa"
    "pais de origen"
}
{encender, apagar, acelerar, tocar bocina, abrir puertas, cerrar puertas, velocidad maxima}

### POLIMORFISMO  === un mismo metodo puede tener diferentes comportamientos dependiendo del objeto que lo invoque

#
clase animal{
ruido()}

obj 1 = perro
ruido() ===> guau guau
obj 2 = gato
ruido() ===> miau miau

class Animal:
    def ruido(self):
        pass # = > es decir, no tiene una implementacion concreta, sino que se espera que las clases hijas lo implementen 
        print("El animal hace un ruido")
        
        
class Perro(Animal):
    def ruido(self):
        return "guau guau"
        print("El perro hace un ruido")

class Gato(Animal):
    def ruido(self):
        return "miau miau"
        print("El gato hace un ruido")

### ABSTRACCION ===> es el proceso de ocultar los detalles de implementacion y mostrar solo la funcionalidad al usuario, 
                # es decir, se enfoca en lo que hace el objeto en lugar de como lo hace

class CuentaBanco:
    def consultar_saldo(self):
        print("El saldo es 2000")
    def retirar_dinero(self, monto):
        print(f"Se ha retirado {monto} del saldo")
    def transferir(self):
        print("Se ha transferido dinero a otra cuenta")
        
### ENCAPSULAMIENTO  === > es el proceso de ocultar los datos y metodos de una clase, 
                        # y solo permitir el acceso a ellos a traves de metodos publicos, es decir, se enfoca en proteger los datos y metodos de una clase 
                        # para evitar que sean modificados o accedidos de manera indebida
                        
class Paciente:
    def __init__(self, nombre, edad, diagnostico):
        self.nombre = nombre
        self.edad = edad
        self.__diagnostico = diagnostico
        
    def ver_diagnostico(self):
        return self.__diagnostico
    
    def cambiar_diagnostico(self, nuevo_diagnostico):
        self.__diagnostico = nuevo_diagnostico
        
paciente1 = Paciente("Juan", 30, "Gripe")
print(paciente1.nombre) # Juan
print(paciente1.edad) # 30

print(paciente1.ver_diagnostico()) # Gripe

paciente1.cambiar_diagnostico("Covid-19")
print(paciente1.ver_diagnostico()) # Covid-19

## otro metodo
class Calculadora:
    def __init__(self):
        self.__resultado = 0
        
    def sumar(self, valor):
        self.__resultado += valor
        
    def restar(self, valor):
        self.__resultado -= valor
        
    def montrar_resultado(self):
        return self.__resultado
    
calc = Calculadora()
calc.sumar(10)
calc.restar(5)
print(calc.mostrar_resultado()) # 5

#### SOLID PRINCIPIOS DE LA PROGRAMACION ORIENTADA A OBJETOS

## S === RESPONSABILIDAD UNICA ===> una clase debe tener una sola responsabilidad, es decir, una sola razon para cambiar, es decir, una sola funcionalidad o tarea que realizar

## O === ABIERTO/CERRADO ===> una clase debe estar abierta para su extension, pero cerrada para su modificacion, es decir, se deben poder agregar nuevas funcionalidades a una clase sin modificar su codigo fuente, es decir, sin modificar la clase original

## L ===> SUSTITUCION DE LISKOV ===> los objetos de una clase derivada deben ser sustituibles por objetos de la clase base, es decir, se deben poder usar objetos de una clase derivada en lugar de objetos de la clase base sin afectar el correcto funcionamiento del programa

## I ===> SEGREGACION DE INTERFACES ===> una clase no debe depender de interfaces que no utiliza, es decir, se deben crear interfaces especificas para cada funcionalidad o tarea que realizar, en lugar de crear una interfaz general que contenga todas las funcionalidades o tareas

## D ===> INVERSION DE DEPENDENCIAS ===> las dependencias deben ser abstraidas, es decir, se deben depender de abstracciones en lugar de depender de concreciones, es decir, se deben crear interfaces o clases abstractas para definir las dependencias, en lugar de depender de clases concretas.