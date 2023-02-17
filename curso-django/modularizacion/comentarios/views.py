from django.shortcuts import render
from django.http import HttpResponse
from. models import Comment

def test(request):
    return HttpResponse("funciona correctamente")


def create (request):
    #comment=Comment(name="Juanjo", score=5, comment="Este es un comentario")
    #comment.save()

    comment=Comment.objects.create(name="alex")
    return HttpResponse ("ruta para probar creación de modelos")

def delete(request):
    #comment=Comment.objects.get(id=4)
    #comment.delete()
    Comment.objects.filter(id=2).delete()

    return HttpResponse("Ruta para probar borrados")

# Create your views here.
