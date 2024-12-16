# Sistema Experto para Evaluación de Gabinetes de Control Eléctrico

Este proyecto implementa un sistema experto en Python para evaluar el estado de un gabinete de control eléctrico según las normativas más exigentes de la industria. El sistema realiza preguntas clasificadas por categorías y genera un reporte detallado en PDF con las áreas que necesitan atención, priorizadas y acompañadas de descripciones técnicas.

---

## Características

- **Preguntas Clasificadas por Categorías**: Las preguntas están organizadas en categorías como Seguridad Eléctrica, Ventilación y Temperatura, Mantenimiento, entre otras.
- **Priorización de Acciones**: Las áreas de mejora se clasifican según su prioridad (Alta, Media, Baja).
- **Descripciones Técnicas Detalladas**: Cada acción incluye una descripción técnica como guía para implementar las mejoras.
- **Reporte en PDF**: Se genera un archivo PDF con toda la información de la evaluación, incluyendo detalles de las áreas que necesitan atención.

---

## Requisitos del Sistema

- **Python 3.8 o superior**
- Librerías necesarias (pueden instalarse con `pip`):
  - `sqlite3` (integrado en Python)
  - [`fpdf`](https://pypi.org/project/fpdf/)

---

## Instalación

1. **Clonar el Repositorio**  
   Clona el repositorio desde GitHub:
   `git clone https://github.com/CChavez27/SE_P3_Proyecto`
   `cd tu_repositorio`
2. **Instalar Dependencias**  
  Instala la librería fpdf:
   `pip install fpdf`

4. **Crear la Base de Datos**
  Ejecuta el script para crear la base de datos:  
   `python crear_base_datos.py`
  

## Uso

  1.**Ejecutar el Sistema Experto**
  Inicia la evaluación ejecutando el archivo principal:
  `python SE_Gabinetes.py`

2.**Responde las Preguntas**
  El sistema hará preguntas relacionadas con el estado del gabinete. Responde con Sí o No.

3.**Generar Reporte en PDF**
Una vez completada la evaluación, se generará un archivo PDF con el reporte en el directorio actual. El nombre del archivo será algo como:
        `reporte_gabinete_añoMesDia_hrminSeg`


##  Personalización
Puedes personalizar las preguntas, reglas, categorías y descripciones modificando el script 
        `crear_base_datos.py.`

## Contribuciones
¡Se aceptan contribuciones! Si encuentras errores o tienes ideas para mejorar el sistema, crea un issue o envía un pull request.

