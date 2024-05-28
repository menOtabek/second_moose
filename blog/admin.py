from django.contrib import admin

from blog.models import Post, Comment, Contact, Category


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    inlines = [PostInline]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_time', 'updated_time')
    list_display_links = ('title', 'author')
    search_fields = ('title', 'author')
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'created_time', 'updated_time')
    list_display_links = ('post', 'name')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_time', 'updated_time')
    list_display_links = ('name', 'email')
    search_fields = ('name', 'email')
