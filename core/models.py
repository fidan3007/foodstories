from django.db import models
from accounts.models import User

class Story(models.Model):
    title = models.CharField(max_length=100)
    desription = models.TextField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey('Category', related_name='stories', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='stories')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='stories', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    desription = models.TextField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    # category
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title
    

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    # user
    text = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name