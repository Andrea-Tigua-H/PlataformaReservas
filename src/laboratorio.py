#      Integrantes:
#Tigua Holguin Nicole Andrea
#Mite Reyes Maira Alejandra
#Rodriguez Llamuca Alexandro Steven
#Viteri Roca Helen Adriana


from src.espacio import Espacio

# Clase Laboratorio:
# Representa un laboratorio en la universidad. Hereda de Espacio.
class Laboratorio(Espacio):
    def validar_disponibilidad(self, hora):
        return super().validar_disponibilidad(hora) # Utiliza la validacion definida en la superclase.

# Pruebas individuales para Laboratorio
if __name__ == "__main__":
    lab = Laboratorio(nombre= "Lab de Computo 2", capacidad= 25, horario_disponible= [("08:00", "16:00")])
    print("Prueba 1 - Disponible a las 12:00 :", lab.validar_disponibilidad("12:00"))
    print("Prueba 2 - Disponible a las 18:00 :", lab.validar_disponibilidad("18:00"))