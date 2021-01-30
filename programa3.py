class banco():

    nombre = None
    lugar = None
    cliente = None
    num_cajeros = None
    seguridad = None
    ventanillas = None
    origen = None
    sucursal = None
    color = None
    turno = None
    
    def init(self):
        print("class banco")
        
    def depositar_dinero(self):
        print("método depositar_dinero")

    def atender_cliente(self):
         print("método atender_cliente")

    def controlar_dinero(self):
        print("método controlar_dinero")

    def ayudar_cliente(self):
        print("método ayudar_cliente")

    def recibir_pagos(self):
        print("método recibir_pagos")

BBVA = coche()
BBVA.nombre = "BBVA Bancomer"
BBVA.lugar = "Tulancingo"
BBVA.cliente = "varios"
BBVA.num_cajeros = "6"
BBVA.seguridad = "alta"
BBVA.ventanillas = "4"
BBVA.origen = "Mexico"
BBVA.sucursal = "2"
BBVA.color = "azul_con_blanco"
BBVA.turno = "varios"

BBVA.depositar_dinero()
BBVA.atender_cliente()
BBVA.controlar_dinero()
BBVA.ayudar_cliente()
BBVA.recibir_pagos()
