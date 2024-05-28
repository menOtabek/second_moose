from django.shortcuts import render, redirect
from .models import Contact, Comment
from blog.models import Post
import requests
from django.core.paginator import Paginator
from django.db.models import Count

BOT_TOKEN = '6387477042:AAEOg7Yz68zwD3YH9jWmwpij7SiUnki_O1E'
CHAT_ID = '5937168278'


def index_view(request):
    posts = Post.objects.annotate(comment_number=Count('comments'))
    context = {
        'posts': posts.order_by('created_time')[:3],
        'home': 'active'
    }

    return render(request, 'index.html', context=context)


def blog_view(request):
    data = request.GET
    cat = data.get('cat')
    page = data.get('page')
    if cat:
        posts = Post.objects.filter(category=cat)
        context = {
            'posts': posts.annotate(comment_number=Count('comments')),
            'blog': 'active',
        }
        return render(request, 'blog.html', context)

    posts = Post.objects.annotate(comment_number=Count('comments'))
    page_obj = Paginator(posts, 3)
    context = {
        'blog': 'active',
        'posts': page_obj.get_page(page)
    }
    return render(request, 'blog.html', context=context)


def about_view(request):
    context = {
        'about': 'active'
    }
    return render(request, 'about.html', context=context)


def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        obj = Contact.objects.create(name=data['name'], email=data['email'], message=data['message'])
        obj.save()
        TEXT = f"""
        From : Moose 2
        id: {obj.id}
        name: {obj.name}
        email: {obj.email}
        message: {obj.message}
        time: {obj.created_time}
        """
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={TEXT}'
        response = requests.get(url)
        print(response)
        return redirect('/contact')

    context = {
        'contact': 'active'
    }

    return render(request, 'contact.html', context=context)


def blog_detail_view(request, pk):
    if request.method == 'POST':
        data = request.POST
        obj = Comment.objects.create(name=data['name'], email=data['email'], message=data['message'], post_id=pk)
        obj.save()
        return redirect(f'/blog/{pk}')
    comments = Comment.objects.filter(post_id=pk, is_visible=True)
    post = Post.objects.get(id=pk)
    post.view_count += 1
    post.save(update_fields=['view_count'])

    context = {
        'post': post,
        'comments': comments,
        'comments_count': len(comments),
        'blog': 'active'
    }

    return render(request, 'blog-single.html', context=context)
