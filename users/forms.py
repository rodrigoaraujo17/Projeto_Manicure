from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Cliente


class ClienteCreationForm(UserCreationForm):

    class Meta:
        model = Cliente
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'cpf',
            'telefone',
        )


class ClienteChangeForm(UserChangeForm):

    class Meta:
        model = Cliente
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'cpf',
            'telefone',
        )
