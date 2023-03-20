from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ClienteCreationForm, ClienteChangeForm
from .models import Cliente


class ClienteAdmin(UserAdmin):
    add_form = ClienteCreationForm
    form = ClienteChangeForm
    model = Cliente
    list_display = ("email", "is_staff", "is_active",)
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Cliente, ClienteAdmin)
