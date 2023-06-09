from django.contrib import admin
from .models import Author, Category, Post, PostCategory, CategorySubscriber


class PostAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in PostCategory._meta.get_fields()]  # список имен полей в админке
    list_display = ('author', 'title', 'text')
    list_filter = ('dateCreation', )
    search_fields = ('name', 'text', 'category__name')
    # actions = [nullfy_post]


# def nullfy_post(modeladmin, request, queryset):
#     category = Category.objects.request(name='category')
#     Post.objects.filter(postCategory__name=category).delete()
#     queryset.update(xxxxx )
# nullfy_post.short_description = 'Обнулить посты'


# class PostCategoryAdmin(admin.ModelAdmin):
#     # list_display = [field.name for field in Category._meta.get_fields()]
#     list_display = 'name'


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(CategorySubscriber)
