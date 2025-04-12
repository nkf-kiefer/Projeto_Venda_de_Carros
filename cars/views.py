#importando uma função que retorna um template para o usuário
from cars.models import Car
#importando da pasta cars/models a classe car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required 
#importando a verificação de login
from django.utils.decorators import method_decorator



#serve para listar os carros e fazer o metodo get além de servir para realizar pesquisas
class CarListView(ListView):
    model = Car #propriedades das classes 
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
       cars = super().get_queryset().order_by('model')  #buscando em todos os carros cadastrados no bd e ordenando eles em ordem pelo modelo
       search = self.request.GET.get('search') #vendo se o usuário filtrou no parâmetro search algo
       if search:
            cars = cars.filter(model__icontains = search) #trazendo do banco de dados todos carros que estão sendo buscados pelo usuário
       return cars #funcao render e passando o html dentro da pasta template como parametro



#formulário para criar carro novo
@method_decorator(login_required(login_url='login'), name='dispatch')#encapsulando a view para que apenas o usuário que esteja logado no sistema consiga acessar
class NewCarCreateView(CreateView):
   model = Car
   form_class = CarModelForm
   template_name = 'new_car.html'
   success_url = '/cars/'


#classe para quando o usuário clicar em um carro para ele ver detalhes do carro
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView): #codigo para atualizar algum dado do carro
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self): #função do django para você jogar em uma url pré definida
        return reverse_lazy('car_detail',kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
