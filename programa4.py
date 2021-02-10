class avion():

 tamano = None
 clase = None
 serie = None
 motor= None
 alas = None
 azafata = None
 piloto = None
 color = None
 capacidad = None 
 llantas = None

 def __init__(self):
   print("Clase avion")

 def volar(self):
   print("Metodo volar")

 def frenar(self):
   print("Metodo frenar")

 def arrancar(self):
   print("Metodo arrancar")

 def aterrizar(self):
   print("Metodo aterrizar")

 def despegar(self):
   print("Metodo despegar")

aeromexico = avion()
aeromexico.tamano = "grande"
aeromexico.clase = "media"
aeromexico.motor = "hidraulico"
aeromexico.alas = "semiflecha"
aeromexico.azafata = "3"
aeromexico.color = "blanco_rojo"
aeromexico.capacidad = "200_personas"
aeromexico.llantas = "r15"

aeromexico.volar()
aeromexico.frenar()
aeromexico.arrancar()
aeromexico.aterrizar()
aeromexico.despegar()
