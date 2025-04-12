from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
    
    def ready(self): #importando ready para o django saber que vai ter signals
        import cars.signals 
    
    