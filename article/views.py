import json
from django.shortcuts import render, render_to_response, get_list_or_404 
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import Context, loader  ,RequestContext
from django.core import serializers 
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from article.models import Article, ArticleCategory, Tag


class ArtileList(ListView):
	model = Article

class ArtileCreate(CreateView):
	model = Article
		

def articles(request):
	data={}
	data['articles'] = Article.objects.all()
	return render(request, 'article/article_list.html', data)

def add_articles(request):
	data={}
	data['articles'] = Article.objects.all() 
	if request.method == 'POST':
		if not request.POST.get('title',False):
			title= ""
		article = Article(title=title,photo=request.FILES['file'])
		article.save()
		result = {"file":article.photo.url}
		response = JSONResponse(result, {}, response_mimetype(request))
		response['Content-Disposition'] = 'inline; filename=files.json'
		return response
		#return HttpResponse(json.dumps(result))
		#return HttpResponseRedirect(reverse('articles'))
	return render_to_response('article/articles.html',data, context_instance=RequestContext(request))


def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"

class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self, obj='', json_opts={}, mimetype="application/json", *args, **kwargs):
        content = json.dumps(obj, **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)


































































	