from django.db.models.signals import post_save,post_delete,pre_save
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum


def car_inventory_update():
    #car objects é padrão
    #isso são querrys no bd
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value

    )

#se a biografia do carro não for adicionada cria uma automatica
@receiver(pre_save,sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Bio gerada automaticamente!'

#quando um carro novo for cadastrado cacula dois valores (quant de carros no estoque e valor total do estoque) e salva no bd 
@receiver(post_save,sender=Car)
def car_post_save(sender,instance,**kwargs):
      car_inventory_update()

#Quando um carro for retirado ele atualiza a quantidade de carros que você tem e o valor deles somados
@receiver(post_delete,sender=Car)
def car_post_delete(sender,instance,**kwargs):
   car_inventory_update()