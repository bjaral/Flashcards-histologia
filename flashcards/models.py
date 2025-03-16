from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='categorias/')
    
    def __str__(self):
        return self.nombre

class Parte(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    imagen_parte = models.ImageField(upload_to='partes/')
    imagen_flashcards = models.ImageField(upload_to='flashcards/') # Todas las flashcards tienen la misma imagen
    
    def __str__(self):
        return self.nombre

class Flashcard(models.Model):
    parte = models.ForeignKey(Parte, on_delete=models.CASCADE)
    pregunta = models.TextField()
    respuesta = models.TextField()
    
    def __str__(self):
        return self.pregunta