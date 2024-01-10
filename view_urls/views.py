from django.http import HttpResponse
from django.shortcuts import render
from . import machine_learning_model
from . import  fake_model;
from . import ml_predict

def  home(request):
    # return HttpResponse("This is a working page!")
    return render(request, 'index.html')
    
def about(request):
     return render(request, 'about.html')
    
def contact(request):
     return render(request, 'contact.html')
    
def resultXXX(request):
   user_input =  request.GET['user_input']
   user_input = machine_learning_model.multiplier(user_input)
   return render(request, 'result.html', {'home_input': user_input})
    
def result(request):
   pclass =  int(request.GET['pclass'])
   sex =  int(request.GET['sex'])
   age =  int(request.GET['age'])
   sibsp =  int(request.GET['sibsp'])
   parch =  int(request.GET['parch'])
   fare =  int(request.GET['fare'])
   embarked =  int(request.GET['embarked'])
   title =  int(request.GET['title'])


   prediction = ml_predict.prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title)
   
   return render(request, 'result.html', {'prediction': prediction})
    
    