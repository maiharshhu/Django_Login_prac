from django.contrib import admin
from .models import User, appdata, user_data

# Register your models here.
class appdataAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'app_link', 'app_points')
    search_fields = ('app_name',)

class userdataAdmin(admin.ModelAdmin):
    list_display = ('user', 'app', 'points', 'screenshot')
    search_fields = ('user', 'app')



# Register the models in the admin panel
admin.site.register(User)
admin.site.register(appdata, appdataAdmin)
admin.site.register(user_data, userdataAdmin)