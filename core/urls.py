from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('story/<int:id>/', story_detail, name='story_detail'),
    path('about/', about, name='about'),
    path('stories/', stories, name='stories'),
    path('recipes/', recipes, name='recipes'),
    path('recipe/<int:id>/', recipe_detail, name='recipe_detail'),
    path('contact', contact, name='contact'),
    path('create-story', create_story, name='create_story'),
    path('create-recipe', create_recipe, name='create_recipe'),
    path('edit-story/<int:pk>/', EditStory.as_view(), name='edit_story'),
    path('edit-recipe/<int:pk>/', EditRecipe.as_view(), name='edit_recipe'),
    path('delete_story/<int:id>/', delete_story, name='delete_story'),
    path('delete_recipe/<int:id>/', delete_recipe, name='delete_recipe'),


]
