from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values':['С вопросмаи по телефону', '(068) 068 88 88', 'asd@gmail.com']})
