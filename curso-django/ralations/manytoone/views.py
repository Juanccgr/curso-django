from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date
# Create your views here.

def create(request):
    reporter= Reporter(first_name='juanjo', last_name='Ruiz',email='juan@demo.com')
    reporter.save()
    art1=Article(headline='Lorem ipsum dolot', pub_date=date(2022.5,5), rep=reporter)
    art1.save()
    art2=Article(headline='Lorem ipsum aimet', pub_date=date(2022.7,1), rep=reporter)
    art2.save()
    art3=Article(headline='Ipsum lorem dolot', pub_date=date(2022.9,4), rep=reporter)
    art3.save()
    
    

    return HttpResponse("Creado")



