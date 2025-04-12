from django.contrib import admin
from cars.models import Car,Brand #importando da pasta cars - a classe Car e Brand

class CarAdmin(admin.ModelAdmin): #classe model admin já pronta
    list_display = ('model','brand','factory_year','model_year','value') #queremos esses campos na busca do admin
    search_fields = ('model',) #se quiser filtrar por outros parametros

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand,BrandAdmin)
admin.site.register(Car,CarAdmin) #salvando da tabela car e importando as propriedades de CarAdmin

