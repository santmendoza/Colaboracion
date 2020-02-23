from Vehiculo import Vehiculo

    #Definimos la clase Carro
class Carro(Vehiculo):
        #Atributos
        def __init__(self, nombre, ruedas, color, modelo, velocidad, cilindraje):
            Vehiculo.__init__(self, nombre,ruedas,color,modelo)
            self.velocidad = velocidad
            self.cilindraje = cilindraje

        def arrancar(self,nombre,cilindraje):
            return print ('Arrancando el carro '+nombre + ' con cilindraje :'+cilindraje)

        def frenar(self,nombre,color):
            return print('El carro de nombre'+nombre+' ha frenado! de color'+color)