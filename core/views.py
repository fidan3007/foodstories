from django.shortcuts import render, redirect
from core.models import *
from core.forms import *


def home(request):
    stories = Story.objects.order_by('-id')[:4]
    last_story = stories.first()
    categories = Category.objects.all()
    holiday = Story.objects.filter(category__title='Holiday')
    context = {
        'stories': stories,
        'last_story': last_story,
        'categories': categories,
        'holiday': holiday,
    }
    return render(request, 'index.html', context)


def story_detail(request, id):
    story = Story.objects.get(id=id)
    categories = Category.objects.all()
    recents = Story.objects.order_by('-id')[:2]
    tags = Tag.objects.all()
    context = {
        'data': story,
        'categories': categories,
        'recents': recents,
        'tags': tags,
    }
    return render(request, 'single.html', context)

def about(request):
    return render(request, 'about.html')


def stories(request):
    search = request.GET.get('search')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    stories = Story.objects.order_by('-id')
    if search:
        stories = stories.filter(title__icontains=search)
    if cat:
        stories = stories.filter(category__title=cat)
    if tag:
        stories = stories.filter(tags__title=tag)
    categories = Category.objects.all()
    context = {
        'stories':stories,
        'categories':categories,
    }
    return render(request, 'stories.html', context)

def recipes(request):
    search = request.GET.get('search')
    recipes = Recipe.objects.order_by('-id')
    if search:
        recipe = recipes.filter(title__icontains=search)
    categories = Category.objects.all()
    context = {
        'recipes':recipes,
        'categories':categories,
    }
    return render(request, 'recipes.html', context)

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    recents = Recipe.objects.order_by('-id')[:2]
    context = {
        'data' : recipe,
        'categories': categories,
        'tags':tags,
        'recent':recents
    }
    return render(request,'single.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ContactForm()
    return render(request, 'contact.html', {'form':form})





