from Vehiculo import Vehiculo

    #Definimos la clase Carro
    class Carro(Vehiculo):
        #Atributos
        def __init__(self, nombre, ruedas, color, modelo, velocidad, cilindraje):
            Vehiculo.__init__(self, nombre,ruedas,color,modelo)
            self.velocidad = velocidad
            self.cilindraje = cilindraje