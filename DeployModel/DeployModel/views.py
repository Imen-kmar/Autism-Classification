from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home (request):
    return render(request,"home.html")

def result(request):

    cls = joblib.load("AutismDecisionTreeClassifier.pkl")
    lis = []
    lis.append(request.GET['Chromosome'])
    lis.append(request.GET['Position'])
    lis.append(request.GET['A'])
    lis.append(request.GET['C'])
    lis.append(request.GET['G'])
    lis.append(request.GET['T'])

    ans = cls.predict([lis])


    return render(request,"result.html",{'ans':ans})