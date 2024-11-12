# core/management/commands/init_db.py
import psycopg2
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Initialize the database'

    def handle(self, *args, **options):
        self.stdout.write('Initializing database...')
        conn = None
        try:
            conn = psycopg2.connect(
                dbname='postgres',
                user=settings.DATABASES['default']['USER'],
                password=settings.DATABASES['default']['PASSWORD'],
                host=settings.DATABASES['default']['HOST'],
                port=settings.DATABASES['default']['PORT'],
            )
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'geoda_dev'")
            exists = cursor.fetchone()
            if not exists:
                cursor.execute('CREATE DATABASE geoda_dev')
                self.stdout.write(self.style.SUCCESS('Database "geoda_dev" created successfully'))
            else:
                self.stdout.write(self.style.SUCCESS('Database "geoda_dev" already exists'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error initializing database: {e}'))
        finally:
            if conn:
                conn.close()