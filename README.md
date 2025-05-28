# 📚 Plataforma de Reservas para Espacios Universitarios

## 👥 Integrantes del Grupo
- Tigua Holguin Nicole Andrea  
- Mite Reyes Maira Alejandra  
- Rodriguez Llamuca Alexandro Steven  
- Viteri Roca Helen Adriana

---

## 📋 Descripción del Proyecto

Este proyecto es una plataforma básica en Python que permite gestionar la disponibilidad de espacios universitarios como:

- Laboratorios
- Salas de estudio
- Auditorios

Se utiliza programación orientada a objetos (POO), aplicando **encapsulamiento**, **herencia** y **polimorfismo**.

---

## ▶️ Instrucciones para Ejecutar el Sistema

### Requisitos
- Tener instalado **Python 3.x**
- Tener un entorno como **PyCharm Community Edition**

### Pasos:
1. Abrir el proyecto en PyCharm.
2. Ejecutar el archivo `main.py` (clic derecho > Run `main.py`)
3. Opcional: ejecutar individualmente cada subclase para ver sus pruebas (`laboratorio.py`, `sala_estudio.py`, `auditorio.py`).

---

## 🧱 Descripción de las Clases

### 🔹 `Espacio` (superclase)
- Atributos: nombre, capacidad, horario disponible.
- Método `validar_disponibilidad(hora)`: verifica si una hora está dentro de un rango definido.

### 🔹 `Laboratorio`, `Sala_Estudio`, `Auditorio`
- Heredan de `Espacio`.
- Pueden sobreescribir o extender el comportamiento.
- Implementan su propia validación usando `super()`.

---

##  Ejemplo de Ejecución

```plaintext
Espacio: Lab Computo, Capacidad: 25, Horarios: [('08:00', '16:00')]
Espacio: Sala B, Capacidad: 20, Horarios: [('10:00', '15:00')]
Espacio: Auditorio 1, Capacidad: 100, Horarios: [('14:00', '16:00')]
¿Esta disponible el Laboratorio a las 10:00? True
¿Esta disponible la Sala de estudio a las 16:00? False
¿Esta disponible el Auditorio a las 12:00? False
```

---

## 📸 Capturas de Pantalla de los Resultados

A continuación se presentan las capturas de pantalla obtenidas desde la consola al ejecutar cada parte del sistema. Esto demuestra el funcionamiento correcto del proyecto.

### 🖥️ Resultado general (`main.py`)

![🖼️ Captura Main](CapturaMain.png)

---

### 🧪 Prueba individual: Laboratorio

![🧪 Laboratorio](CapturaLaboratorio.png)

---

### 🧪 Prueba individual: Sala de Estudio

![📚 Sala de Estudio](CapturaSalaEstudio.png)

---

### 🧪 Prueba individual: Auditorio

![🎤 Auditorio](CapturaAuditorio.png)