from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model): #class car que está herdando de uma classe já criada pelo proprio django
    id = models.AutoField(primary_key=True) #criando um id para a classe carro
    model = models.CharField(max_length=200) #modelo do carro em string
    brand =models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand") #chave estrangeira
    factory_year = models.IntegerField(blank=True, null=True) #usando int
    model_year = models.IntegerField(blank=True, null=True) #se quiser deixar em branco
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True) #usando float
    photo = models.ImageField(upload_to="cars/", blank=True, null=True) #toda foto que subir armazene na raiz do projeto
    bio = models.TextField(blank=True, null=True)#texto de quem tá vendendo o carro sendo ele somente opcional 

    def __str__(self):
        return self.model
    #retorna o nome do carro

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    #esse campo armazena data e hora que foi criado esse registro
    
    class Meta:
        ordering = ['-created_at']
        #ordenando de forma decrescente o registro de car inventory para mostrar do criado por ultimo para o primeiro

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
    #mostrando a quantidade de carros e a soma do valor de todos 
    

