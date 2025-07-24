from django.contrib import admin



from .models import CameraLocation

@admin.action(description="Approve selected camera locations")
def approve_locations(modeladmin, request, queryset):
    queryset.update(approved=True)

@admin.register(CameraLocation)
class CameraLocationAdmin(admin.ModelAdmin):
    list_display = ("description", "latitude", "longitude", "approved", "created_at")
    list_filter = ("approved",)
    actions = [approve_locations]
