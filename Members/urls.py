from django.urls import path, include
from . import views as member_views


urlpatterns = [
    path('', member_views.login_user, name='login'),
    path('logout', member_views.logout_user, name='logout'),
]