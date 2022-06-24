from django.shortcuts import render
from django.views import generic
from website.models import Article
from backend.models import MProductionWork, MCustomWork, MStoreInventory

# Create your views here.
def index(request):
  context = {'prodo': MProductionWork.objects.all()}
  return render(request, 'index.html', context)

def about(request):
  return render(request, 'about.html')

def pads(request):
  return render(request, 'pads.html')

def articles(request):
  context = {
    'article': Article.objects.all(),
  }
  return render(request, 'articles.html', context)

class ArticleDetail(generic.DetailView):
  model = Article

def shop(request):
  context = {
    'prodo': MProductionWork.objects.all(),
    'customwork': MCustomWork.objects.all(),
    'storeInventory': MStoreInventory.objects.all(),
  }
  return render(request, 'shop.html', context)