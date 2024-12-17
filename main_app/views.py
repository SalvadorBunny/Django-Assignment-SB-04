from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class AddClientView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'create_cliente.html'
    
class UpdateClientView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'create_cliente.html'
    
# class DeleteClientView(DeleteView):
#     model= Cliente
#     template_name = 'delete_client.html'
#     success_url = reverse_lazy('index')

class ListClientView(ListView):
    model = Cliente
    template_name = 'lista_cliente.html'
    context_object_name = 'clientes'

def delete_client(request, pk):
    clientes= Cliente.objects.get(pk=pk)
    clientes.delete()
    return redirect('list_client')

def search_client(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        clientes = Cliente.objects.filter(nombre__contains= searched)
        return render(request,
                      'lista_cliente.html',
                      {'searched': searched,
                       'clientes' : clientes
                       })
    else:
        return redirect('list_client')