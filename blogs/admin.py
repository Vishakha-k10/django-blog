from django.contrib import admin
from  .models import Category
from  .models import Blog , Comment 
class  BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('title',)}
    list_display=('title','author','category','status','is_featured','created_at')
    search_fields=('title','author__username','category__category_name','status')
    list_editable=('status','is_featured')


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
# Register your models here.
