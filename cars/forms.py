from django import forms
from cars.models import Brand, Car

class CarModelForm(forms.ModelForm): #criando um form em cima da tabela car
    class Meta:
        model = Car #todos os campos da tabela car
        fields = '__all__' #pegando todos os campos do model e criar um formulário
        
    def clean_value(self): #função de validação de campo no caso valor
        value = self.cleaned_data.get('value') #capturando o valor que o usuário digitou
        if value < 20000: #se o valor for menor que 20.000
            self.add_error('Value','Valor minímo do carro deve ser de R$20.000') #adiciona um erro no próprio form
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error("factory_year",'O ano de fabricação aceitável é de até 1975!')
        return factory_year

