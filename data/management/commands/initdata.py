from django.contrib.auth.models import User
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Load data from json file."

    def handle(self, *args, **options):
        call_command("loaddata", "./fixtures/data.json")
