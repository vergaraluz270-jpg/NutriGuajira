# NutriGuajira 🌿

Sistema experto de valoración nutricional para instituciones educativas y fundaciones en La Guajira, Colombia.

## Descripción

NutriGuajira es una aplicación web desarrollada con Django que apoya a nutricionistas en la valoración y seguimiento nutricional de niños en zonas vulnerables. El sistema combina un motor de inferencia basado en reglas expertas con inteligencia artificial (Groq LLaMA) para generar planes alimentarios personalizados usando los insumos del Programa de Alimentación Escolar (PAE).

## Problema que resuelve

La Guajira ocupa el primer lugar en desnutrición crónica infantil en Colombia. Las fundaciones y colegios reciben suministros mensuales del PAE pero carecen de herramientas para gestionar la alimentación individualizada. NutriGuajira es ese puente tecnológico.

## Funcionalidades

- Registro de pacientes con datos clínicos, alergias y representante legal
- Cálculo automático de IMC en tiempo real
- Motor de inferencia basado en reglas expertas editables
- Generación de planes alimentarios personalizados con IA (Groq LLaMA 3.3)
- Seguimiento mensual con gráfica de evolución del IMC
- Dashboard con estadísticas y distribución nutricional
- Panel de administración para gestionar reglas y catálogo PAE

## Tecnologías

- Python 3.12
- Django 5.x
- SQLite
- Bootstrap 5
- Chart.js
- Groq API (LLaMA 3.3 70B)
- python-dotenv

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/vergaraluz270-jpg/NutriGuajira.git
cd NutriGuajira

# 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
# Crear archivo .env con:
# SECRET_KEY=tu_secret_key
# GROQ_API_KEY=tu_groq_api_key
# DEBUG=True

# 5. Aplicar migraciones
python manage.py migrate

# 6. Cargar datos iniciales
python manage.py loaddata apps/recomendaciones/fixtures/datos_iniciales.json
python manage.py loaddata apps/valoracion/fixtures/reglas.json

# 7. Crear superusuario
python manage.py createsuperuser

# 8. Correr el servidor
python manage.py runserver
```

## Uso de IA

- **Claude (Anthropic):** Apoyo en diseño de modelos relacionales, estructura del proyecto Django, motor de inferencia, vistas y templates HTML.
- **Groq LLaMA 3.3 70B:** Integrado dentro de la app para generar planes alimentarios personalizados basados en los datos clínicos del paciente, sus alergias y el catálogo PAE disponible mensualmente.

## Integrantes

- Luz Vergara
- Luis Torres
- Jose Yanes
- Dewis Álvarez

**Universidad de La Guajira — Programación Avanzada 2026-I**  
**Docente: Eduardo Sierra**