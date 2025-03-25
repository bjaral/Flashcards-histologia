from django.db import models

def parte_image_path(instance, filename):
    return f'partes/{instance.nombre}/{filename}'

def parte_flashcard_path(instance, filename):
    return f'flashcards/{instance.nombre}/{filename}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='categorias')
    
    def __str__(self):
        return self.nombre

class Parte(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    imagen_parte = models.ImageField(upload_to=parte_image_path)
    imagen_flashcards = models.ImageField(upload_to=parte_flashcard_path) # Todas las flashcards tienen la misma imagen
    
    def __str__(self):
        return f"({self.categoria.nombre}) {self.nombre}"

class Flashcard(models.Model):
    parte = models.ForeignKey(Parte, on_delete=models.CASCADE)
    pregunta = models.TextField()
    respuesta = models.TextField()
    
    def __str__(self):
        return f"({self.parte.nombre}) {self.pregunta}"