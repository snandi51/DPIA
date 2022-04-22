from django.urls import path, include
from . import views as member_views
from Assessment import views as assessment_views


urlpatterns = [
    path('', member_views.login_user, name='login'),
    path('logout', member_views.logout_user, name='logout'),
    path('screening', assessment_views.screening, name='screening'),
    path('dpia_screening', assessment_views.dpia_screening, name='dpia_screening'),

]