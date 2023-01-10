from django.shortcuts import render 
from ventehabbi.models import Article 

def home(request):
    article =Article.objects.all()
    if request.method =="GET":
        name=request.GET.get('recherche')
        if name is not None:
        
         article =Article.objects.filter(title__icontains=name)
    context={
        'articles':article,
        'message':'bienvenue sur mon site d\'exposition des fruits'
    }
    return render(request,'index.html',context)


