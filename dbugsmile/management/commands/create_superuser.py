import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Crear superusuario de forma segura al desplegar la app en el hosting."

    def handle(self, *args, **kwargs):
        username = os.environ.get('KERNELUSER')
        email = os.environ.get('KERNELEMAIL')
        password = os.environ.get('KERNELPASSWORD')

        if not (username and email and password):
            self.stderr.write(self.style.ERROR("No se han definido todas las variables de entorno necesarias."))
            return

        try:
            user, created = User.objects.get_or_create(username=username, email=email)
            if created:
                user.set_password(password)
                self.stdout.write(self.style.SUCCESS(password))
                user.is_staff = True
                user.is_superuser = True
                user.save()
                self.stdout.write(self.style.SUCCESS("SuperUsuario creado correctamente."))
            else:
                self.stdout.write("El SuperUsuario ya existe.")
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error al crear el SuperUsuario: {e}"))