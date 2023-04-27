from django.urls import path
from .views import *


urlpatterns = [
    path('',home, name='home'),
    path('receipe/',receipe, name='receipe'),
    path('details/',viewReceipe, name='view-receipe'),
    path('delete/<str:id>/',deleteReceipe, name='delete-receipe'),
    path('update/<str:id>/',updateReceipe, name='update-receipe'),
    path('login/', login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('signup/', register, name='signup'),
]