#      Integrantes:
#Tigua Holguin Nicole Andrea
#Mite Reyes Maira Alejandra
#Rodriguez Llamuca Alexandro Steven
#Viteri Roca Helen Adriana


from src.espacio import Espacio

# Clase Auditorio:
# Representa un auditorio en la universidad. Hereda de Espacio.
class Auditorio(Espacio):
    def validar_disponibilidad(self, hora):
        return super().validar_disponibilidad(hora) # Utiliza la validacion definida en la superclase.

# Pruebas individuales para Auditorio
if __name__ == "__main__":
    aud = Auditorio(nombre= "Auditorio 4", capacidad= 80, horario_disponible= [("14:00", "16:00")])
    print("Prueba 1 - Disponible a las 12:00 :", aud.validar_disponibilidad("12:00"))
    print("Prueba 2 - Disponible a las 18:00 :", aud.validar_disponibilidad("18:00"))