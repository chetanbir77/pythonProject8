from django.contrib import admin
from .models import covid_vaccine_statewise_mode,covid_india,statewise_testing

admin.site.register(covid_vaccine_statewise_mode)
admin.site.register(covid_india)
admin.site.register(statewise_testing)
# Register your models here.
