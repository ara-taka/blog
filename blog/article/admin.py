from django.contrib import admin
from .models import Article, Category

# Register your models here.
class CategoryInlineAdmin(admin.StackedInline):
    """
    ArticleモデルとCategoryモデルのオブジェクトを同時に登録する。
    extraはCategoryオブジェクト登録の表示件数。
    """
    model = Category
    extra = 1

class ArticleModelAdmin(admin.ModelAdmin):
    # 管理サイトのArticle一覧表示のフィールドを変更
    list_display = ('id', 'title', 'create_date', 'update_date')
    inlines = [CategoryInlineAdmin]

class CategoryModelAdmin(admin.ModelAdmin):
    # 管理サイトのCategory一覧表示のフィールドを変更
    list_display = ('article', 'genre')


admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Category, CategoryModelAdmin)