from django.contrib import admin
from .models import Elections
from .models import Selection

# Register your models here.
admin.site.register(Elections)
admin.site.register(Selection)