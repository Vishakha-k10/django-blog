

from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from  .models import Blog , Category 


def posts_by_category(request, category_id):
    #fetch the posts  that belongs to the category with the id category_id 
    posts=Blog.objects.filter(status='Published', category=category_id)
    #using  try/except to do  some custom action if category deosnt exist 
    #try:
    #   category= Category.objects.get(pk=category_id)
    #except:
    #   return redirect('home') #redirecting the user to homepage 
    # use get_object_or_404 when we want to show 404 error page if category doesnt exist 
    category=get_object_or_404(Category,pk=category_id)
    context={
        'posts': posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context)
