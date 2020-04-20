from django.contrib import admin
from blog.models import Post, Comments, Category


# Register your models here.

class CommentInline(admin.TabularInline):
	model=Comments
	extra=3
class PostAdmin(admin.ModelAdmin):
	fieldsets=[
			(None, {'fields':['title']}),
			(None,{'fields':['body']}),
			(None,{'fields':['categories']}),
			]
	date_create=Post.created_on
	date_update=Post.last_modified

	inlines=[CommentInline]



	
class CategoryAdmin(admin.ModelAdmin):
	pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
