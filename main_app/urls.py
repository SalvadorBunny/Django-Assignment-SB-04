from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from . import views
from .views import IndexView, AddClientView, UpdateClientView, ListClientView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clients/list/', login_required(ListClientView.as_view()), name='list_client'),
    path('clients/add/', staff_member_required(AddClientView.as_view()), name='add_client'),
    path('clients/update/<int:pk>', staff_member_required(UpdateClientView.as_view()), name='update_client'),
    path('clients/delete/<int:pk>', staff_member_required(views.delete_client), name='delete_client'),
    path('clients/search/', login_required(views.search_client), name='search_client'),
]