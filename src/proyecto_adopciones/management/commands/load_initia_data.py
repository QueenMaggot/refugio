# src/proyecto_adopciones/management/commands/load_initial_data.py
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
import os

class Command(BaseCommand):
    help = "Carga backup_utf8.json si la base de datos está vacía"

    def handle(self, *args, **options):
        # Verificar si ya hay usuarios
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM auth_user")
            count = cursor.fetchone()[0]

        if count == 0:
            # backup_utf8.json está en src/
            fixture_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                'backup_utf8.json'
            )
            if os.path.exists(fixture_path):
                self.stdout.write("🔍 Cargando datos iniciales desde backup_utf8.json...")
                call_command('loaddata', fixture_path, verbosity=2)
                self.stdout.write(self.style.SUCCESS("✅ Datos cargados con éxito."))
            else:
                self.stdout.write(self.style.ERROR(f"❌ Archivo no encontrado: {fixture_path}"))
        else:
            self.stdout.write("ℹ️  La base ya tiene datos. No se carga el fixture.")