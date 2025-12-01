# src/proyecto_adopciones/management/commands/load_initial_data.py
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
from pathlib import Path

class Command(BaseCommand):
    help = "Carga backup_utf8.json si la base de datos está vacía"

    def handle(self, *args, **options):
        # Verificar si ya hay usuarios
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM auth_user")
            count = cursor.fetchone()[0]

        if count == 0:
            # Ruta: src/backup_utf8.json
            current_file = Path(__file__).resolve()
            src_dir = current_file.parent.parent.parent.parent  # sube 4 niveles
            fixture_path = src_dir / "backup_utf8.json"

            if fixture_path.exists():
                self.stdout.write(f"🔍 Cargando desde: {fixture_path}")
                call_command('loaddata', str(fixture_path), verbosity=2)
                self.stdout.write(self.style.SUCCESS("✅ Datos cargados."))
            else:
                self.stdout.write(self.style.ERROR(f"❌ Fixture no encontrado: {fixture_path}"))
        else:
            self.stdout.write("ℹ️  La base ya tiene datos.")