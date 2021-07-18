from django.contrib import admin
from .models import AllsafeWebsite
@admin.register(AllsafeWebsite)
class AllsafeWebsiteAdmin(admin.ModelAdmin):
    list_display=["date","time","status","total_request"]