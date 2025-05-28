#      Integrantes:
#Tigua Holguin Nicole Andrea
#Mite Reyes Maira Alejandra
#Rodriguez Llamuca Alexandro Steven
#Viteri Roca Helen Adriana

# Clase Espacio:
# Clase base que representa un espacio universitario, con nombre, capacidad y horarios disponibles.

class Espacio:
    def __init__(self, nombre, capacidad, horario_disponible):
        # Constructor que inicializa los atributos del espacio.
        self._nombre = nombre
        self._capacidad = capacidad
        self._horario_disponible = horario_disponible # Lista de tuplas con rangos de horas.

    def __str__(self):
        # Metodo para representar el objeto como texto.
        return f'Espacio: {self._nombre}, Capacidad: {self._capacidad}, Horarios: {self._horario_disponible}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, capacidad):
        self._capacidad = capacidad

    @property
    def horario_disponible(self):
        return self._horario_disponible

    @horario_disponible.setter
    def horario_disponible(self, horario_disponible):
        self._horario_disponible = horario_disponible

    def validar_disponibilidad(self, hora):
        # Revisa si una hora esta dentro de alguno de los rangos disponibles.
        for inicio, fin in self._horario_disponible:
            if inicio <= hora <= fin:
                return True
        return False