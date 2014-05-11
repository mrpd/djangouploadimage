from django.contrib import admin
from       .models  import fileUp, something

class AdminCeo(admin.ModelAdmin):
#    class Meta:
#        models=Ceo
    model=fileUp    
admin.site.register(fileUp, AdminCeo)    

class Adminsom(admin.ModelAdmin):
    model=  something
admin.site.register(something, Adminsom)   