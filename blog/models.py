from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    author = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author_image = models.ImageField(upload_to='images/', blank=True, null=True)
    view_count = models.IntegerField(default=0)

    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    email = models.EmailField()
    name = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)

    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
