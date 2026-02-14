from django.urls import path
from . import views

urlpatterns = [
    path('landing/', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('college/<int:id>/', views.college_detail, name='college_detail'),
    path('fav/<int:id>/', views.add_fav),
    path('ai-chat/', views.ai_chat),
]
