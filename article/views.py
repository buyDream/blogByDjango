from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404

def test(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})   
# return render(request, 'test.html', {'current_time': datetime.now()})

def home(request):
   # return HttpResponse("Hello World, Django")
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})
#def detail(request, my_args):
 #   post = Article.objects.all()[int(my_args)]
  #  str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))
   # return HttpResponse(str)
 #   return HttpResponse("Your're looking at my_args %s." % my_args)
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})
# Create your views here.
