class estudiante():

nombre = None
edad = None
sexo = None
matricula = None
uniforme = None
calzado = None
instituto = None
carrera = None
num_asignaturas = None

    def init(self):
        print("class estudiante")
        
    def participar(self):
        print("método participar")

    def estudiar(self):
         print("método estudiar")

    def realizar_actividades(self):
        print("método realizar_actividades")

    def asistir_clase(self):
        print("método asistir_clase")

    def poner_atención(self):
        print("método poner_atencion")


alumno = estudiante()
alumno.nombre = "Itzel"
alumno.edad = "18"
alumno.sexo = "mujer"
alumno.matricula = "1720110219"
alumno.uniforme = "jumper"
alumno.calzado = "zapato_escolar"
alumno.instituto = "UTEC"
alumno.carrera = "TIC_21"
alumno.num_asignaturas = "8"

alumno.participar()
alumno.estudiar()
alumno.realizar_actividades()
alumno.asistir_clase()
alumno.poner_atencion()
