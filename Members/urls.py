from django.urls import path, include
from . import views as member_views
from Assessment import views as assessment_views


urlpatterns = [
    path('', member_views.login_user, name='login'),
    path('logout', member_views.logout_user, name='logout'),
    path('screening', assessment_views.screening, name='screening'),
    path('index', assessment_views.home, name='index'),
    path('result', assessment_views.result, name='result'),
    path('dpia_screening', assessment_views.dpia_screening, name='dpia_screening'),
    path('risk_summary', assessment_views.risk_summary, name='risk_summary'),
    path('heat_map', assessment_views.heat_map, name='heat_map'),

]