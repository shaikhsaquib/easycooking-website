from django.shortcuts import render,HttpResponse
from app_two.models import recipie
from .forms import RecipeForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def service1(request):
    if request.method == 'POST':
        search= request.POST.get('talash')
        search=recipie.objects.filter(RecipeName__icontains=search)
        return render(request, 'service1.html',{'re':search})
    else:
        return render(request,'service1.html')

def service2(request):
    if request.method == 'POST':
        search= request.POST.get('talash')
        search=recipie.objects.filter(TranslatedIngredients__icontains=search)
        return render(request, 'service2.html',{'re':search})
    else:
        return render(request,'service2.html')
    
def service3(request):
    return render(request,'service3.html')