from django.shortcuts import render,HttpResponse, get_object_or_404,redirect
from .models import author, category, article
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def index(request):
    post=article.objects.all()
    context={
        "post":post
    }
    return render(request, "index.html", context)

def getauthor(request, name):
    return render(request, "profile.html")

def getsingle(request, id):
    post=get_object_or_404(article, pk=id)
    first=article.objects.first()
    last=article.objects.last()
    related=article.objects.filter(category=post.category).exclude(id=id)[:4]
    context={
        "post":post,
        "first":first,
        "last":last,
        "related":related
    }
    return render(request, "single.html", context)
def getTopic(request, name):
    cat=get_object_or_404(category,name=name)
    post=article.objects.filter(category=cat.id)

    return render(request, "category.html",{"post":post, "cat":cat})

def getlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('password')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')
    return render(request, "login.html")


def getlogout(request):
    logout(request)
    return redirect('index')

