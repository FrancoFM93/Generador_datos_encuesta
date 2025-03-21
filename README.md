Generador de Datos de Encuesta sobre Tecnologías Digitales

Este proyecto genera datos simulados para una encuesta sobre el uso y la percepción de las tecnologías digitales en el ámbito académico y laboral. Los datos generados incluyen respuestas a preguntas relacionadas con el tiempo de uso de herramientas digitales, la efectividad percibida, las interrupciones y la satisfacción general.
Características

    Genera datos simulados para 100 respuestas de encuesta.

    Incluye información como:

        Id: Identificador único para cada respuesta.

        Start time y Completion time: Fechas y horas simuladas para el inicio y finalización de la encuesta.

        Email: Correos electrónicos generados aleatoriamente con formatos específicos (e.g., @inacapmail.cl o @gmail.com).

        Name: Nombres completos generados aleatoriamente.

        Respuestas a preguntas: Datos simulados para preguntas relacionadas con el uso de tecnologías digitales.

Requisitos

    Python 3.x

    Bibliotecas necesarias:

        faker

        pandas

        random

        datetime

Instala las dependencias con el siguiente comando:
bash
Copy

pip install faker pandas

Uso

    Clona este repositorio:
    bash
    Copy

    git clone https://github.com/FrancoFM93/Generador_datos_encuesta.git
    cd Generador_datos_encuesta

    Ejecuta el script para generar los datos:
    bash
    Copy

    python generador_encuesta.py

    El archivo de salida (Encuesta_Tecnologias_Digitales.xlsx) se guardará en la ruta especificada en el código (C:/Users/franc/OneDrive/Escritorio/vs/estadistica/).

Estructura del Archivo de Salida

El archivo Excel generado contiene las siguientes columnas:
Columna	Descripción
Id	Identificador único de la respuesta.
Start time	Fecha y hora de inicio de la encuesta.
Completion time	Fecha y hora de finalización de la encuesta.
Email	Correo electrónico generado aleatoriamente.
Name	Nombre completo generado aleatoriamente.
¿Cuántas horas al día utiliza tecnologías digitales para actividades relacionadas con sus estudios o su trabajo?	Horas diarias de uso de tecnologías digitales (valor entero entre 1 y 12).
¿Cuántas herramientas digitales diferentes utiliza regularmente (aplicaciones, software, etc.)?	Número de herramientas utilizadas (valor entero entre 1 y 10).
¿Cuántas horas a la semana dedica a buscar soluciones técnicas o aprender sobre nuevas herramientas digitales?	Horas semanales dedicadas a aprendizaje técnico (valor entero entre 0 y 20).
¿Consideras que las herramientas digitales que usa actualmente son efectivas para mejorar su productividad?	Respuesta categórica: "Sí" o "No".
¿Crees que las tecnologías digitales han reducido el tiempo que necesita para realizar tareas importantes?	Respuesta categórica: "Sí" o "No".
¿Considera que las interrupciones relacionadas con tecnologías digitales (notificaciones, problemas de conectividad, fallos técnicos, etc.) afectan su productividad?	Respuesta categórica: "Sí" o "No".
¿Qué tan satisfecho está con el impacto de las tecnologías digitales en su organización diaria?	Respuesta categórica: "Muy satisfecho", "Satisfecho", "Neutro", "Insatisfecho", "Muy insatisfecho".
Personalización

    Número de respuestas: Cambia el valor de n_responses en el código para generar más o menos respuestas.

    Rango de fechas: Modifica las fechas en generate_random_date() para ajustar el período de tiempo simulado.

    Probabilidad de correos @inacapmail.cl: Ajusta el parámetro inacap_probability en generate_random_email().

Contribuciones

Si deseas contribuir a este proyecto, ¡no dudes en hacer un fork y enviar un pull request! Todas las contribuciones son bienvenidas.
Licencia

Este proyecto está bajo la licencia MIT.

This README.md provides a clear and concise overview of your project, making it easy for others to understand and use. Let me know if you need further adjustments!
