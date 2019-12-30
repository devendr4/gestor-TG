from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy

#importando vistas genéricas
#las vistas genéricas ayudan a ahorrar código
#en caso de que no existan se utilizan funciones
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from ..decorators import admin_permissions
from django.contrib.auth.decorators import login_required

from ..models import User


'''TODO-> VER COMO RESTRINGIR ENTRE SÍ LA ELECCIÓN DEL TIPO DE USUARIO EN LOS FORMULARIOS'''


#sin contraseña para agregarla solo en la creación
USER_CRUD_FIELDS = [
    "username",
    "first_name",
    "last_name",
    "email",
    "is_active",
    "date_joined",
    "is_admin",
    "is_manager",
    "is_guest"
]

#evitar sobreescritura de la instancia "user" de las sesiones
USER_CRUD_CONTEXT_OBJECT_NAME = "user_context_object"


@method_decorator([login_required, admin_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/user/index.html'
    context_object_name = 'users_list'
    
    def get_queryset(self):
        return User.objects.order_by('id')[:10]


@method_decorator([login_required, admin_permissions], name='dispatch')
class DetailView(generic.DetailView):
    model = User
    template_name = 'managerApp/user/detail.html'
    context_object_name = USER_CRUD_CONTEXT_OBJECT_NAME


@method_decorator([login_required, admin_permissions], name='dispatch')
class CreateUserView(generic.CreateView):
    model = User
    CREATE_FIELDS = USER_CRUD_FIELDS.copy()
    CREATE_FIELDS.insert(0,'password')
    fields = CREATE_FIELDS
    template_name = 'managerApp/user/create.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        messages.success(self.request, 'Fue creado un nuevo usuario')
        return redirect('user:user_list')



@method_decorator([login_required, admin_permissions], name='dispatch')
class UpdateUserView(generic.UpdateView):
    model = User
    fields = USER_CRUD_FIELDS
    template_name = 'managerApp/user/update.html'
    context_object_name = USER_CRUD_CONTEXT_OBJECT_NAME

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save_without_hashing()
        messages.success(self.request, 'Fue actualizado un usuario')
        return redirect('user:user_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class DeleteUserView(generic.DeleteView):
    model = User
    template_name = 'managerApp/user/delete.html'
    success_url = reverse_lazy('user:user_list')
    context_object_name = USER_CRUD_CONTEXT_OBJECT_NAME
