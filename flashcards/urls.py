from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # Categorías URLs
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<int:categoria_id>/', views.categoria_detalle, name='categoria_detalle'),
    
    # Flashcards URLs
    path('flashcards/', views.flashcards, name='flashcards'),
    path('flashcards/parte/<int:parte_id>/', views.parte_detalle, name='parte_detalle'),
    path('flashcards/estudiar/<int:parte_id>/', views.estudiar_flashcards, name='estudiar_flashcards'),
    path('flashcards/estudiar/<int:parte_id>/<int:flashcard_id>/', views.estudiar_flashcards, name='estudiar_flashcard_especifica'),
    path('flashcards/resultados/<str:resultados>/', views.resultados, name='resultados'),
    
    # Sobre nosotros
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
]