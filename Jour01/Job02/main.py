class Operation:
    #init = constructeur
    def __init__(self, nombre1 = 12, nombre2 = 3):

        self.nombre1 = nombre1
        self.nombre2 = nombre2


operation_instance = Operation()

#resultat de la classe
print ("le nombre1 est " + str (operation_instance.nombre1))
print ("le nombre2 est " + str (operation_instance.nombre2))