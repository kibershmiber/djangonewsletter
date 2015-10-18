from django.contrib import admin

# Register your models here.

from .models import SingUp
from .forms import SingUpForm

class SingUpAdmin(admin.ModelAdmin):
    "Shows a SingUp Form in an admin place"

    list_display = ["__str__", "full_name"]
    form = SingUpForm
    #class Meta:
     #   model = SingUp

admin.site.register(SingUp, SingUpAdmin)