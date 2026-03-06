
#Para cada ejercicio construir un programa Python declarando 4 atributos y 2 métodos:
#1. clase ANIMAL e instancie un objeto llamado GATO
class Animal:
    edad=10
    peso=5
    nombre="Pacho"
    color="Naranja"
    def años(self):
        print(f"El gato tiene {self.edad} de edad")
    def estado(self):
        if self.peso>5:
            print("Gato en sobrepeso")
        elif self.peso<5:
            print("Gato bajo de peso")
        else:
            print("Gato en peso ideal")

gato=Animal()
gato.años()
gato.estado()

#2. clase VEHICULO e instancie un objeto llamado MOTO.
#3. clase VEHÍCULO e instancie un objeto llamado CARRO.
class Vehiculo:
    color="Azul"
    marca="Yamaha"
    año=2005
    def tipo(self,marca):
        self.marca=marca
    def años(self,año):
        self.año=año
moto=Vehiculo()
carro=Vehiculo()
carro.tipo("BMW")
carro.años(2000)
print(f"El color del carro es {carro.color}")
print(f"El color de la moto es {moto.color}")
print(f"Año del carro {carro.año}")
print(f"Año del moto {moto.año}")
print(f"El tipo del carro es {carro.marca}")
print(f"El tipo de la moto es {moto.marca}")
#4. clase COMIDA e instancie un objeto llamado BANDEJA PAISA.
class Comida:
    lugar=10
    =5
    nombre="Pacho"
    color="Naranja"
    def años(self):
        print(f"El gato tiene {self.edad} de edad")
    def estado(self):
        if self.peso>5:
            print("Gato en sobrepeso")
        elif self.peso<5:
            print("Gato bajo de peso")
        else:
            print("Gato en peso ideal")

gato=Animal()
gato.años()
gato.estado()
#5. clase ARBOL e instancie un objeto llamado PINO.
#6. clase LIBRO e instancie un objeto llamado NOVELA.
#7. clase PELICULA e instancie un objeto llamado MONSTERSINC.
#8. clase DISPOSITIVO e instancie un objeto llamado PORTATIL.
#9. clase SERVICIO e instancie un objeto llamado ENERGÍA.
#10. clase EMPAQUE e instancie un objeto llamado CAJA.
#11. clase PERSONA e instancie un objeto llamado ESTUDIANTE