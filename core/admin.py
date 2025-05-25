from django.contrib import admin
from core.models import *

admin.site.register([Category, Tag, Recipe, Story, Comment, Contact,])
