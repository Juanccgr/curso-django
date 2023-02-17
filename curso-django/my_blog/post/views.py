from django.shortcuts import render
from django.http import HttpResponse
from .models import Author,Entry

def queries(request):
    #obtener todos los elementos
    author=Author.objects.all()

    #obtener datos filtrados por condición
    filtered=Author.objects.filter(email='larry')

    ##obtener un único elemento filtrado
    authors=Author.objects.get(id=1)

    #Obtener los 10 primeros elementos
    limit=Author.objects.all()[:10]

    #obterner 10 elementos, saltando los 5 primeros
    offsets=Author.objects.all()[5:10]

    #obtener elementos ordenados por email
    orders=Author.objects.all().order_by('email')

    #obtener elementos cuyo id sea menor o igual a 15
    filtered2=Author.objects.filter(id__lte=15)

    #obtener todos los autores que contienen en su nombre la palabra yes
    filtered3=Author.objects.filter(name__contain='yes')




    return render(request, 'post/queries.html',{'author':author, 'filtered':filtered})
