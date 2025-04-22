from django.shortcuts import render
from .models import Parte, Categoria, Flashcard
from django.http import JsonResponse
from django.db import connections
from django.conf import settings

# Create your views here.
def inicio(request):
    return render(request, 'home.html')

def categorias(request):
    categorias = Categoria.objects.all()  # Obtener todas las categorías de flashcard de la base de datos
    return render(request, 'categories/categories.html', {'categorias': categorias})

def categoria_detalle(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    partes = Parte.objects.filter(categoria=categoria)
    return render(request, 'categories/category_detail.html', {
        'categoria': categoria,
        'partes': partes
    })

def flashcards(request):
    partes = Parte.objects.all()  # Obtener todas las partes de flashcard de la base de datos
    return render(request, 'flashcards/parts.html', {'partes': partes})

def parte_detalle(request, parte_id):
    parte = Parte.objects.get(id=parte_id)
    flashcards = Flashcard.objects.filter(parte=parte)
    return render(request, 'flashcards/part_detail.html', {
        'parte': parte,
        'flashcards': flashcards
    })

def resultados(request, resultados):
    import json
    
    # Decodificar los resultados JSON
    try:
        resultados_dict = json.loads(resultados)
        
        # Obtener las flashcards correspondientes
        flashcard_ids = list(resultados_dict.keys())
        flashcards_list = Flashcard.objects.filter(id__in=flashcard_ids)
        
        # Organizar las flashcards por categoría de conocimiento
        conocidas = []
        mas_o_menos = []
        no_conocidas = []
        
        for flashcard in flashcards_list:
            score = int(resultados_dict.get(str(flashcard.id), 0))
            if score == 2:
                conocidas.append(flashcard)
            elif score == 1:
                mas_o_menos.append(flashcard)
            else:
                no_conocidas.append(flashcard)
        
        # Obtener la parte para el botón de volver a estudiar
        parte_id = flashcards_list[0].parte.id if flashcards_list else None
        
        context = {
            'conocidas': conocidas,
            'mas_o_menos': mas_o_menos,
            'no_conocidas': no_conocidas,
            'parte_id': parte_id,
            'total_conocidas': len(conocidas),
            'total_mas_o_menos': len(mas_o_menos),
            'total_no_conocidas': len(no_conocidas)
        }
        
    except (json.JSONDecodeError, ValueError):
        context = {
            'error': 'Formato de resultados inválido'
        }
    
    return render(request, 'flashcards/results.html', context)

def estudiar_flashcards(request, parte_id, flashcard_id=None):
    parte = Parte.objects.get(id=parte_id)
    flashcards = Flashcard.objects.filter(parte=parte)
    
    # Si se especifica una flashcard, la buscamos
    current_flashcard = None
    if flashcard_id:
        try:
            current_flashcard = flashcards.get(id=flashcard_id)
            current_index = list(flashcards).index(current_flashcard)
        except Flashcard.DoesNotExist:
            current_index = 0
    else:
        current_index = 0
    
    return render(request, 'flashcards/study_flashcards.html', {
        'parte': parte,
        'flashcards': flashcards,
        'current_index': current_index
    })

def sobre_nosotros(request):
    return render(request, 'about.html')

def db_info(request):
    """Vista para mostrar información de la base de datos actual."""
    db_info = {
        'engine': settings.DATABASES['default']['ENGINE'],
        'name': str(settings.DATABASES['default']['NAME']),  # Convert WindowsPath to string
        'host': settings.DATABASES['default'].get('HOST', 'N/A'),
        'using_sqlite': 'sqlite' in settings.DATABASES['default']['ENGINE'],
        'tables': []
    }
    
    # Obtener lista de tablas
    with connections['default'].cursor() as cursor:
        if 'sqlite' in settings.DATABASES['default']['ENGINE']:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        else:
            cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        db_info['tables'] = [table[0] for table in tables]
    
    return JsonResponse(db_info)