from django.urls import path
from .views import index_view, blog_view, about_view, contact_view, blog_detail_view


urlpatterns = [
    path('', index_view),
    path('blog/', blog_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('blog/<int:pk>/', blog_detail_view)
]