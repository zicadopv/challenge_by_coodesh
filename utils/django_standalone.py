import django, os, sys
from django.conf import settings
sys.path.append("challenge_by_coodesh")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_space_flight.settings")

# settings.configure(DEBUG=True)
django.setup()

from voos.models import Voo, Launch, Events

