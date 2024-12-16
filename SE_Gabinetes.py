import sqlite3
from fpdf import FPDF
import datetime

def conectar_base_datos(ruta_bd):
    try:
        return sqlite3.connect(ruta_bd)
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def cargar_preguntas_y_acciones(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.pregunta, r.accion, p.categoria
        FROM preguntas p
        JOIN reglas r ON p.regla_id = r.id
        ORDER BY p.categoria ASC, p.id ASC
    """)
    return cursor.fetchall()

def preguntar(pregunta):
    while True:
        respuesta = input(f"{pregunta} (Sí/No): ").strip().lower()
        if respuesta in ['sí', 'si', 'no']:
            return respuesta in ['sí', 'si']
        print("Por favor, responde con 'Sí' o 'No'.")

def evaluar_respuestas(preguntas_y_acciones):
    """
    Evalúa las respuestas del usuario y lista las áreas de mejora.
    """
    areas_mejora = []
    categoria_actual = None  # Variable para rastrear la categoría actual

    for pregunta, accion, categoria in preguntas_y_acciones:
        # Mostrar la categoría si cambia
        if categoria != categoria_actual:
            if categoria_actual is not None:
                print("\n")  # Espaciado entre categorías
            print(f"Categoría: {categoria}")
            categoria_actual = categoria

        # Realizar la pregunta
        respuesta = preguntar(pregunta)
        if not respuesta:  # Si la respuesta es "No"
            areas_mejora.append((accion, categoria))

    return areas_mejora

def generar_pdf(info_maquina, areas_mejora, conn):
    """
    Genera un archivo PDF con el reporte de la evaluación, incluyendo descripciones detalladas de las acciones necesarias.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Reporte de Evaluación del Gabinete de Control', 0, 1, 'C')
    pdf.ln(10)

    # Información de la máquina
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, 'Información de la Máquina:', 0, 1)
    for key, value in info_maquina.items():
        pdf.cell(0, 10, f'{key}: {value}', 0, 1)
    pdf.ln(10)

    # Detalles de la evaluación
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Áreas que necesitan atención (ordenadas por categoría):', 0, 1)
    pdf.set_font('Arial', '', 12)

    if areas_mejora:
        # Agrupar por categoría
        categorias_ordenadas = {}
        for area, categoria in areas_mejora:
            if categoria not in categorias_ordenadas:
                categorias_ordenadas[categoria] = []
            categorias_ordenadas[categoria].append(area)

        # Escribir las áreas agrupadas por categoría
        for categoria, areas in sorted(categorias_ordenadas.items()):
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 10, f"\nCategoría: {categoria}", 0, 1)
            pdf.set_font('Arial', '', 12)
            for area in areas:
                # Recuperar la descripción desde la base de datos
                cursor = conn.cursor()
                cursor.execute("SELECT descripcion FROM reglas WHERE accion = ?", (area,))
                descripcion = cursor.fetchone()[0]

                # Escribir el área con la descripción
                pdf.multi_cell(0, 10, f"  - {area}\n      Descripción: {descripcion}")
                pdf.ln(5)

        # Resetear color para el texto general
        pdf.set_text_color(0, 0, 0)
    else:
        pdf.cell(0, 10, "¡El gabinete cumple con todos los estándares!", 0, 1)

    # Guardar el PDF
    fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_pdf = f"reporte_gabinete_{fecha}.pdf"
    pdf.output(nombre_pdf)
    print(f"Reporte generado: {nombre_pdf}")


def main():
    ruta_bd = "sistema_experto.db"
    conn = conectar_base_datos(ruta_bd)
    if conn is None:
        print("Error al conectar con la base de datos.")
        return

    print("Por favor, ingrese la información de la máquina:")
    info_maquina = {
        "Nombre de la Máquina": input("Nombre de la Máquina: "),
        "Número de Serie": input("Número de Serie: "),
        "Ubicación": input("Ubicación: "),
        "Técnico Evaluador": input("Nombre del Técnico Evaluador: "),
        "Fecha de Evaluación": datetime.datetime.now().strftime("%Y-%m-%d")
    }

    preguntas_y_acciones = cargar_preguntas_y_acciones(conn)
    if not preguntas_y_acciones:
        print("No se encontraron preguntas en la base de datos.")
        return

    areas_mejora = evaluar_respuestas(preguntas_y_acciones)
    generar_pdf(info_maquina, areas_mejora, conn)
    conn.close()

if __name__ == "__main__":
    main()
