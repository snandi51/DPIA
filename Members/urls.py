from django.urls import path, include
from . import views as member_views
from Assessment import views as assessment_views


urlpatterns = [
    path('', member_views.login_user, name='login'),
    path('logout', member_views.logout_user, name='logout'),
    path('screening1', assessment_views.screening1, name='screening1'),
    path('screening', assessment_views.screening, name='screening'),
    path('index', assessment_views.home, name='index'),
    path('no_session', assessment_views.no_session, name='no_session'),
    path('pdf', assessment_views.get_pdf, name='pdf'),
    path('result', assessment_views.result, name='result'),
    path('dpia_screening', assessment_views.dpia_screening, name='dpia_screening'),
    path('session_screen', assessment_views.session_screen, name='session_screen'),
    path('risk_summary', assessment_views.risk_summary, name='risk_summary'),
    path('heat_map', assessment_views.heat_map, name='heat_map'),

]