import os
from django.core.management import call_command
from django.db import connection
from django.apps import apps

def load_initial_data_if_needed():
    """
    Carga backup_utf8.json solo si la base de datos está vacía.
    """
    # Verificar si ya hay datos en alguna tabla principal (ej. auth_user o tu modelo Adopter)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM auth_user")
            user_count = cursor.fetchone()[0]
        if user_count == 0:
            fixture_path = os.path.join(os.path.dirname(__file__), '..', 'backup_utf8.json')
            if os.path.exists(fixture_path):
                print("🔍 Base de datos vacía. Cargando datos iniciales...")
                call_command('loaddata', fixture_path, verbosity=2)
            else:
                print("⚠️  Fixture no encontrado:", fixture_path)
        else:
            print("✅ Base de datos ya contiene datos. No se carga fixture.")
    except Exception as e:
        print("❌ Error al verificar/cargar datos iniciales:", e)