from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import ClienteCreationForm


class ClienteCreateView(CreateView):
    template_name = 'users/signup.html'
    form_class = ClienteCreationForm
    success_url = reverse_lazy('manicure:index')
