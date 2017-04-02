from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Community


admin.site.register(Community, PageAdmin)