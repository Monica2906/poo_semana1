class coche():

    color = None
    serie = None
    marca = None
    modelo = None
    transmision = None
    llantas = None
    origen = None
    placa = None
    velocidades = None
    mecanismo = None
    
    def _init_(self):
        print("class coche")
        
    def encender(self):
        print("método encender")

    def avanzar(self):
         print("método avanzar")

    def girar_izquierda(self):
        print("método girar_izquierda")

    def reversa(self):
        print("método reversa")

    def frenar(self):
        print("método frenar")


tsuru = coche()
tsuru.color = "gris con 2 franjas negras"
tsuru.serie = "UA23548E12"
tsuru.marca = "NISSAN"
tsuru.modelo = "tsuru"
tsuru.transmision = "estándar"
tsuru.llantas = "rin 13"
tsuru.origen = "empresa"
tsuru.placa = "HH54JA2"
tsuru.velocidades = "5 velocidades"
tsuru.mecanismo = "dirección mecanica"

tsuru.encender()
tsuru.avanzar()
tsuru.girar_izquierda()
tsuru.reversa()
tsuru.frenar()
