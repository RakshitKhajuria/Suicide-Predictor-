from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,'home.html')

def result (request):

    reg = joblib.load('djangosuicidemodel.sav')

    lst = []
    lst.append(request.GET['Year'])


    print(lst)

    ans = reg.predict([lst])
    
    return render(request, 'result.html',{'ans':ans, 'lst':lst})

