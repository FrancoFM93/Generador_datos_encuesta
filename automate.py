from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta

# Configurar Faker
fake = Faker("es_CL")

# Crear estructura del DataFrame
columns = [
    "Id",
    "Start time",
    "Completion time",
    "Email",
    "Name",
    "¿Cuántas horas al día utiliza tecnologías digitales para actividades relacionadas con sus estudios o su trabajo?",
    "¿Cuántas herramientas digitales diferentes utiliza regularmente (aplicaciones, software, etc.)?",
    "¿Cuántas horas a la semana dedica a buscar soluciones técnicas o aprender sobre nuevas herramientas digitales?",
    "¿Consideras que las herramientas digitales que usa actualmente son efectivas para mejorar su productividad?",
    "¿Crees que las tecnologías digitales han reducido el tiempo que necesita para realizar tareas importantes?",
    "¿Considera que las interrupciones relacionadas con tecnologías digitales (notificaciones, problemas de conectividad, fallos técnicos, etc.) afectan su productividad?",
    "¿Qué tan satisfecho está con el impacto de las tecnologías digitales en su organización diaria?"
]

# Función para generar fechas aleatorias entre el 3 y el 7 de diciembre de 2024
def generate_random_date():
    start_date = datetime(2024, 12, 3)
    end_date = datetime(2024, 12, 7)
    return fake.date_time_between(start_date=start_date, end_date=end_date)

# Función para generar correos con formato específico
def generate_random_email(first_name, last_name, inacap_probability=0.5):
    # Generamos un número aleatorio entre 0 y 1
    second_last_name = fake.last_name() if random.random() < 0.5 else ""  # Generar segundo apellido aleatorio
    
    if random.random() < inacap_probability:
        # Generamos correo @inacapmail.cl con formato nombre.apellidoXX@inacapmail.cl
        email = f"{first_name.lower()}.{last_name.lower()}{random.randint(10, 99)}@inacapmail.cl"
        
        # Nombre con segundo apellido en la columna Name (en mayúsculas)
        name = f"{first_name.upper()} {last_name.upper()} {second_last_name.upper()}" if second_last_name else f"{first_name.upper()} {last_name.upper()}"
        
        return email, name
    else:
        # Generamos correo @gmail.com sin punto entre nombre y apellido
        if random.random() < 0.5:  # 50% de las veces, apellido primero
            email = f"{last_name.lower()}{first_name.lower()}{random.choice([random.randint(10, 99), ''])}@gmail.com"
        else:
            email = f"{first_name.lower()}{last_name.lower()}{random.choice([random.randint(10, 99), ''])}@gmail.com"
        
        # Para @gmail.com, solo generamos primer nombre y primer apellido
        name = f"{first_name} {last_name}"
        
        # En algunos casos, agregamos el segundo apellido aleatorio (aproximadamente 30% de las veces)
        if random.random() < 0.3:
            name += f" {fake.last_name()}"
        
        return email, name

# Generar los datos simulados
n_responses = 100
data = []

# Generar los datos de las respuestas
for i in range(1, n_responses + 1):
    first_name = fake.first_name()
    last_name = fake.last_name()
    
    # Generamos el nombre completo (con segundo apellido aleatorio en algunos casos)
    name = f"{first_name} {last_name}" if random.random() > 0.3 else f"{first_name} {last_name} {fake.last_name()}"
    
    # Usamos el nombre para generar el email, asegurándonos de que coincidan
    email, name = generate_random_email(first_name, last_name, random.random() * 0.7)
    
    # Generamos las fechas
    start_time = generate_random_date()
    completion_time = start_time + timedelta(minutes=random.randint(1, 5))
    
    # Formatear fechas en formato correcto para el DataFrame
    start_time_str = start_time.strftime("%m/%d/%Y %H:%M")
    completion_time_str = completion_time.strftime("%m/%d/%Y %H:%M")
    
    # Respuestas simuladas
    hours_per_day = random.randint(1, 12)
    tools_used = random.randint(1, 10)
    learning_hours = random.randint(0, 20)
    effective_tools = random.choice(["Sí", "No"])
    reduced_time = random.choice(["Sí", "No"])
    interruptions = random.choice(["Sí", "No"])
    satisfaction = random.choice(["Muy satisfecho", "Satisfecho", "Neutro", "Insatisfecho", "Muy insatisfecho"])
    
    # Agregar fila de datos
    data.append([
        i,
        start_time_str,
        completion_time_str,
        email,
        name,
        hours_per_day,
        tools_used,
        learning_hours,
        effective_tools,
        reduced_time,
        interruptions,
        satisfaction
    ])

# Crear DataFrame
df = pd.DataFrame(data, columns=columns)

# Guardar como archivo Excel
file_path = "C:/Users/franc/OneDrive/Escritorio/vs/estadistica/Encuesta_Tecnologias_Digitales.xlsx"
df.to_excel(file_path, index=False)

print(f"Archivo guardado en: {file_path}")
