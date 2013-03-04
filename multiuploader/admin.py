from models import MultiuploaderFile
from django.contrib import admin

class MultiuploaderImageAdmin(admin.ModelAdmin):
    search_fields = ["filename", "key_data"]
    list_display = ["filename", "file", "key_data"]
    list_filter = ["filename", "file", "key_data"]

admin.site.register(MultiuploaderFile, MultiuploaderFileAdmin)