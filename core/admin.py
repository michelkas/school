from django.contrib import admin
from django.conf import settings
from .models import Core
from .forms import CoreForm

@admin.register(Core)
class CoreAdmin(admin.ModelAdmin):
    form = CoreForm
    list_display = ['official_name', 'number', 'promo']


admin.site.site_header = settings.ADMIN_SITE_HEADER 
admin.site.site_title = settings.ADMIN_SITE_TITLE 
   


