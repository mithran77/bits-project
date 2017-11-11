import os # pragma: no cover
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weddingPlanner.settings") # pragma: no cover

from django.core.wsgi import get_wsgi_application # pragma: no cover
from whitenoise.django import DjangoWhiteNoise # pragma: no cover
application = get_wsgi_application() # pragma: no cover
application = DjangoWhiteNoise(application) # pragma: no cover
