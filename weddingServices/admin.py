from django.contrib import admin
from .models import Florist, Caterer, Hall

# Register your models here.
admin.site.register(Hall)
admin.site.register(Caterer)
admin.site.register(Florist)
