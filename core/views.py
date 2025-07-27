from django.shortcuts import render, redirect
from core.models import *
from core.forms import *
from django.views.generic import UpdateView
from django.urls import reverse_lazy


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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.story = Story.objects.get(id=id)
            comment.user = request.user
            comment.save()
            return redirect('core:story_detail', id=id)
    story = Story.objects.get(id=id)
    form = CommentForm()
    categories = Category.objects.all()
    recents = Story.objects.order_by('-id')[:2]
    tags = Tag.objects.all()
    context = {
        'data': story,
        'categories': categories,
        'recents': recents,
        'tags': tags,
        'form': form,
        }
    return render(request, 'single.html', context)

def about(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'about.html', context)



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
    return render(request,'single-recipe.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ContactForm()
    categories = Category.objects.all()
    context = {
        'categories':categories,
        'form':form
    }
    return render(request, 'contact.html', context)

def create_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save()
            story.user = request.user
            story.save()
            return redirect('accounts:profile', id=request.user.id)
    form = StoryForm()
    context = {
        'form':form
    }
    return render(request, 'create-story.html', context)

def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            recipe.user = request.user
            recipe.save()
            return redirect(f'/accounts/profile/{request.user.id}/#resept')
    form = RecipeForm()
    context = {
        'form':form
    }
    return render(request, 'create-recipe.html', context)

class EditStory(UpdateView):
    template_name = "create-story.html"
    model = Story
    form_class = StoryForm
    
    def get_success_url(self):
        return reverse_lazy('accounts:profile', args=[self.request.user.id])

class EditRecipe(UpdateView):
    template_name = "create-recipe.html"
    model = Recipe
    form_class = RecipeForm
    
    def get_success_url(self):
        return reverse_lazy('accounts:profile', args=[self.request.user.id])

def delete_story(request, id):
    story = Story.objects.get(id=id)
    story.delete()
    return redirect('accounts:profile', id=request.user.id)

def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('accounts:profile', id=request.user.id)







