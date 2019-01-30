from django.shortcuts import render, redirect
from .models import Question,Comment

# Create your views here.
def index(request):
    questions = Question.objects.all()
    
    return render(request,"question/index.html",{"questions":questions})
    
def new(request):
    return render(request,"question/new.html")
    
def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    
    Question.objects.create(title=title,content=content)
    
    return redirect("/questions/")
    
def read(request,id):
    question = Question.objects.get(pk=id)
    return render(request,"question/read.html",{"question":question})

def comment_create(request,id):
    question = Question.objects.get(pk=id)
    content = request.POST.get("content")
    
    Comment.objects.create(question=question,content=content)
    
    return redirect(f"/questions/{id}/")


