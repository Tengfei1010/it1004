from django.contrib import admin

from .models import Author, Category, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('category_text', 'sub_category', 'is_valid')
    list_display = ('category_text', 'sub_category', 'created', 'updated', 'is_valid')
    list_filter = ['created', 'is_valid']
    search_fields = ['category_text']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # TODO: update in get fields.....
    list_display = ('name', 'url', 'created', 'updated', 'is_valid')
    list_filter = ['created', 'is_valid']
    search_fields = ['name']
    # must be used readonly_fields.....
    readonly_fields = ['avatar_tag']

    def get_fields(self, request, obj=None):
        if not obj:
            self.fields = ('name', 'url', 'avatar')
        else:
            self.fields = ('name', 'url', 'avatar_tag', 'avatar')
        return super().get_fields(request, obj)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'categories', 'content')
    list_display = ('title', 'author', 'get_categories', 'support', 'tread',
                    'created', 'updated', 'is_valid')
    list_filter = ['created', 'is_valid']
    search_fields = ['title', 'author']

    def get_categories(self, obj):
        return ','.join(c.category_text for c in obj.categories.all())

    get_categories.short_description = '文章分类'
