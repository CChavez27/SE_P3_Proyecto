import sqlite3

def crear_base_datos_completa():
    """
    Crea la base de datos desde cero con preguntas, reglas, categorías, prioridades y descripciones.
    """
    # Ruta de la base de datos
    ruta_bd = "sistema_experto.db"

    # Conectar a la base de datos
    conn = sqlite3.connect(ruta_bd)
    cursor = conn.cursor()

    # Crear tabla de reglas con la columna descripción
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reglas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        accion TEXT NOT NULL,
        prioridad TEXT NOT NULL,
        descripcion TEXT NOT NULL
    )
    """)

    # Crear tabla de preguntas con categoría
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS preguntas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT NOT NULL,
        regla_id INTEGER NOT NULL,
        categoria TEXT NOT NULL,
        FOREIGN KEY (regla_id) REFERENCES reglas (id)
    )
    """)

    # Limpiar tablas existentes
    cursor.execute("DELETE FROM preguntas")
    cursor.execute("DELETE FROM reglas")

    # Insertar reglas con prioridades y descripciones
    reglas = [
    ('Instalar un sistema de desconexión visible y accesible', 'Alta', 
     "Instale un interruptor de desconexión claramente visible, como un interruptor termomagnético, una pastilla de corte o un pulsador de parada de emergencia con indicador LED. Asegúrese de que el dispositivo cumpla con las normativas IEC 60947-2."),
    
    ('Agregar dispositivos de protección adecuados', 'Alta', 
     "Incorpore breakers de calidad industrial, fusibles rápidos o relés térmicos en cada circuito crítico. Para motores eléctricos, considere el uso de relés de sobrecarga ajustables y fusibles con curva adecuada."),
    
    ('Revisar y aislar correctamente los cables expuestos', 'Media', 
     "Use tubos termoencogibles o cinta auto-fusionante en las uniones expuestas. Asegúrese de que el material aislante cumpla con las normativas IEC 60227 para aislamiento de conductores."),
    
    ('Asegurar una conexión a tierra segura y comprobada', 'Alta', 
     "Instale un sistema de puesta a tierra con barras de cobre y asegúrese de que la resistencia a tierra sea menor a 5 ohmios. Utilice conectores adecuados, como bornes de presión o tornillos de tierra."),
    
    ('Organizar el cableado usando ductos', 'Media', 
     "Use ductos ranurados o canales tipo Legrand para organizar los cables. Separe los cables de potencia de los de señal en rutas distintas para evitar interferencias."),
    
    ('Etiquetar todos los componentes de manera clara', 'Baja', 
     "Utilice etiquetas de vinilo termoimpresas resistentes al calor y la humedad. Los sistemas de etiquetado como Brother P-touch son ideales para esta tarea."),
    
    ('Instalar amarres o abrazaderas para asegurar el cableado', 'Baja', 
     "Fije los cables con abrazaderas de nylon o clips metálicos resistentes al calor. Asegúrese de que los amarres cumplan con la clasificación UL 94V-2 para retardancia a la flama."),
    
    ('Asegurar espacio para mantenimiento y expansiones', 'Baja', 
     "Deje un 20% del espacio libre en el gabinete para futuras expansiones. Use rieles DIN adicionales para acomodar componentes nuevos."),
    
    ('Instalar ventiladores o rejillas de ventilación', 'Media', 
     "Incorpore ventiladores con filtros antipolvo y rejillas de ventilación en la parte superior del gabinete. Considere ventiladores con control de velocidad según la temperatura."),
    
    ('Agregar sistemas de ventilación para evitar sobrecalentamiento', 'Media', 
     "Use ventiladores con termostatos o sistemas de enfriamiento activo como intercambiadores de calor. Considere ventiladores NMB-MAT con flujo de aire ajustable."),
    
    ('Instalar un gabinete con clasificación IP adecuada', 'Alta', 
     "Elija gabinetes con clasificación IP54 para entornos con polvo y salpicaduras, o IP65 para áreas expuestas al agua. Prefiera materiales resistentes como acero galvanizado o ABS."),
    
    ('Reemplazar componentes no certificados por alternativas aprobadas', 'Alta', 
     "Sustituya componentes por aquellos certificados bajo estándares UL, CE o IEC. Ejemplos incluyen contactores Schneider, Siemens o ABB."),
    
    ('Asegurarse de que todos los componentes cumplen las especificaciones', 'Alta', 
     "Verifique que cada componente esté diseñado para soportar el voltaje y corriente nominal del sistema. Use software como ETAP para realizar estudios eléctricos."),
    
    ('Proteger conexiones y bornes expuestos', 'Alta', 
     "Instale cubiertas plásticas sobre bornes y terminales expuestos. Considere el uso de protectores retráctiles o cajas encapsuladas."),
    
    ('Verificar que los conductores tengan el calibre adecuado', 'Alta', 
     "Use cables de cobre con calibre de acuerdo con la carga (AWG o mm²). Consulte la tabla de la norma IEC 60364-5-52 para seleccionar el calibre correcto."),
    
    ('Separar rutas de cables de potencia y señal para evitar interferencias', 'Media', 
     "Instale canaletas separadas para cables de señal y potencia. Use cables apantallados en circuitos de señal para reducir el ruido electromagnético."),
    
    ('Sustituir cables por opciones retardantes de flama y baja emisión de humos', 'Alta', 
     "Reemplace los cables existentes por opciones con certificación LSZH (Low Smoke Zero Halogen). Ejemplo: cables Belden 9504."),
    
    ('Garantizar acceso fácil para mantenimiento', 'Media', 
     "Asegúrese de que todos los componentes sean accesibles sin necesidad de desmontar el gabinete. Instale puertas o paneles desmontables."),
    
    ('Implementar sistemas de monitoreo de temperatura', 'Media', 
     "Use sensores de temperatura digitales como los modelos PT100 con PLCs. Considere alarmas visuales y auditivas para temperaturas críticas."),
    
    ('Rediseñar el gabinete para incluir espacio adicional', 'Baja', 
     "Amplíe el diseño con gabinetes modulares para alojar componentes futuros. Evalúe opciones con puertas dobles para facilitar el acceso."),
    
    ('Crear un registro detallado de mantenimiento preventivo y correctivo', 'Alta', 
     "Documente las actividades de mantenimiento en un software como CMMS (Computerized Maintenance Management System)."),
    
    ('Realizar pruebas de aislamiento y continuidad según la IEC 60204-1', 'Alta', 
     "Use un megger para medir el aislamiento y un multímetro para verificar la continuidad de los circuitos."),
    
    ('Implementar sistemas de enclavamiento para evitar acceso no autorizado', 'Alta', 
     "Instale cerraduras con llave o sistemas de enclavamiento eléctricos compatibles con controladores de acceso."),
    
    ('Agregar señalización adecuada para componentes de riesgo', 'Baja', 
     "Use etiquetas y señales de advertencia de alta visibilidad. Cumpla con los colores y pictogramas según ISO 7010."),
    
    ('Instalar barreras físicas para evitar contacto accidental', 'Alta', 
     "Coloque protectores de policarbonato o acrílico sobre componentes energizados. Asegúrese de que sean desmontables para mantenimiento."),
    
    ('Añadir supresores de picos de tensión en las líneas de alimentación', 'Alta', 
     "Instale supresores de sobretensión tipo SPD (Surge Protection Device) clase I o II, como los de Schneider Electric."),
    
    ('Realizar pruebas regulares de resistencia a tierra', 'Media', 
     "Use un medidor de resistencia de tierra para verificar valores menores a 5 ohmios. Realice pruebas al menos cada 6 meses."),
    
    ('Agregar indicadores visuales para advertencias críticas', 'Media', 
     "Incorpore balizas o luces de advertencia para condiciones de fallo o sobrecarga."),
    
    ('Proteger el gabinete contra la entrada de insectos y pequeños animales', 'Media', 
     "Instale sellos de goma o espuma en las aberturas. Use rejillas con malla metálica fina."),
    
    ('Actualizar materiales para garantizar resistencia a la radiación UV', 'Media', 
     "Sustituya el gabinete por uno fabricado en acero inoxidable o polímeros tratados para resistencia UV."),
    
    ('Incorporar sensores redundantes para monitoreo térmico', 'Media', 
     "Implemente sensores duales para monitoreo redundante y configure alarmas independientes para seguridad adicional."),
    
    ('Utilizar disipadores de calor para componentes críticos', 'Media', 
     "Instale disipadores pasivos o ventiladores activos en variadores de frecuencia y transformadores."),
    
    ('Crear acceso simplificado para puntos de conexión a tierra', 'Media', 
     "Incluya terminales de tierra accesibles en la parte inferior del gabinete."),
    
    ('Agregar etiquetas QR o RFID para documentaciones técnicas', 'Media', 
     "Coloque etiquetas QR o RFID que enlacen a manuales y esquemas eléctricos digitales."),
    
    ('Implementar conectores rápidos para mayor confiabilidad', 'Baja', 
     "Sustituya terminales atornilladas por conectores tipo WAGO para reducir tiempos de instalación y mejorar la confiabilidad."),
    ] 

    cursor.executemany("INSERT INTO reglas (accion, prioridad, descripcion) VALUES (?, ?, ?)", reglas)

    # Insertar preguntas con sus categorías
    preguntas = [
        ('¿El gabinete tiene un sistema de desconexión de energía claramente identificado?', 1, 'Seguridad Eléctrica'),
        ('¿Se usan dispositivos de protección como fusibles, breakers o relevadores térmicos?', 2, 'Seguridad Eléctrica'),
        ('¿Todos los cables están debidamente aislados y protegidos contra contacto accidental?', 3, 'Seguridad Eléctrica'),
        ('¿El sistema cuenta con una conexión a tierra adecuada y verificada?', 4, 'Seguridad Eléctrica'),
        ('¿Los cables están organizados en ductos o canales?', 5, 'Organización Interna'),
        ('¿Los componentes están etiquetados correctamente y las etiquetas son legibles?', 6, 'Organización Interna'),
        ('¿Se utilizan abrazaderas o amarres para sujetar los cables y evitar movimientos?', 7, 'Organización Interna'),
        ('¿Se han dejado márgenes suficientes para el mantenimiento y futuras expansiones?', 8, 'Organización Interna'),
        ('¿El gabinete tiene ventilación adecuada para disipar el calor generado por los componentes?', 9, 'Ventilación y Temperatura'),
        ('¿Se utilizan ventiladores, rejillas o sistemas de refrigeración cuando es necesario?', 10, 'Protección Ambiental'),
        ('¿El gabinete está protegido contra polvo y humedad según su entorno (IP54, IP65, etc.)?', 11, 'Protección Ambiental'),
        ('¿Se utilizan componentes certificados (UL, CE, etc.)?', 12, 'Seguridad Eléctrica'),
        ('¿Todos los componentes tienen especificaciones adecuadas para el voltaje y corriente del sistema?', 13, 'Seguridad Eléctrica'),
        ('¿Las conexiones y bornes están protegidos contra contacto directo?', 14, 'Seguridad Eléctrica'),
        ('¿Los conductores tienen el calibre correcto según la carga esperada?', 15, 'Seguridad Eléctrica'),
        ('¿Las rutas de cables están separadas entre potencia y señal para evitar interferencias?', 16, 'Organización Interna'),
        ('¿Los cables cumplen con normativas contra incendios (IEC 60332)?', 17, 'Protección Ambiental'),
        ('¿El sistema tiene acceso fácil para mantenimiento?', 18, 'Mantenimiento'),
        ('¿El gabinete tiene sistemas de monitoreo de temperatura para prevenir sobrecalentamientos?', 19, 'Ventilación y Temperatura'),
        ('¿El diseño permite la expansión futura del sistema?', 20, 'Ventilación y Temperatura'),
        ('¿El gabinete tiene un historial documentado de mantenimiento y fallos?', 21, 'Mantenimiento'),
        ('¿Se han realizado pruebas de puesta en marcha, como aislamiento y continuidad?', 22, 'Normativas de Diseño'),
        ('¿El gabinete cuenta con sistemas de enclavamiento para evitar acceso no autorizado?', 23, 'Normativas de Diseño'),
        ('¿Se utiliza señalización adecuada para componentes de riesgo?', 24, 'Normativas de Diseño'),
        ('¿El gabinete incluye barreras físicas para evitar contacto accidental con componentes energizados?', 25, 'Seguridad Eléctrica'),
        ('¿Se han instalado supresores de picos de tensión en las líneas de alimentación?', 26, 'Seguridad Eléctrica'),
        ('¿Se realizan pruebas regulares de resistencia a tierra?', 27, 'Seguridad Eléctrica'),
        ('¿El gabinete cuenta con indicadores visuales de advertencias críticas?', 28, 'Seguridad Eléctrica'),
        ('¿El gabinete está protegido contra insectos y pequeños animales?', 29, 'Protección Ambiental'),
        ('¿El gabinete incluye materiales resistentes a la radiación UV?', 30, 'Protección Ambiental'),
        ('¿Se han implementado sensores redundantes para monitoreo térmico?', 31, 'Ventilación y Temperatura'),
        ('¿Los componentes críticos tienen disipadores de calor instalados?', 32, 'Ventilación y Temperatura'),
        ('¿Se tiene acceso simplificado a los puntos de conexión a tierra?', 33, 'Mantenimiento'),
        ('¿Se incluyen etiquetas QR o RFID para documentación técnica?', 34, 'Documentación'),
        ('¿Se utilizan conectores rápidos en lugar de terminales atornillados?', 35, 'Organización Interna'),
    ]
    cursor.executemany("INSERT INTO preguntas (pregunta, regla_id, categoria) VALUES (?, ?, ?)", preguntas)

    # Guardar cambios y cerrar conexión
    conn.commit()
    conn.close()

    print("Base de datos creada exitosamente con preguntas, categorías, prioridades y descripciones.")

if __name__ == "__main__":
    crear_base_datos_completa()