from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

import os


class Command(BaseCommand):
    help = "Crear superusuario de forma segura, al desplegar la app en el hosting."

    def handle(self, *args, **kwargs):
        username = os.environ.get('KERNELUSER')
        email = os.environ.get('KERNELEMAIL')
        password = os.environ.get('KERNELPASSWORD')

        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"SuperUsuario creado correctamente."))
