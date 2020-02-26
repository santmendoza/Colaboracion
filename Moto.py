from Vehiculo import Vehiculo

class Moto(Vehiculo):
    #LLamamos al constructor del padre y le asignamos el nuevo atributo
    def __init__(self,nombre,ruedas,color,modelo,cilindraje):
        #Luego creamos el nuevo constructor con el nuevo atributo
        Vehiculo.__init__ (self,nombre,ruedas,color,modelo)
        self.cilindraje=cilindraje


    def arrancar(self,nombre,cilindraje):
        return print ('Arrancando la moto '+nombre + ' con cilindraje :'+cilindraje)

    def frenar(self,nombre,color):
        return print('La moto de nombre'+nombre+' ha frenado! de color'+color)

    def acerlerar(self):
        pass

    






        